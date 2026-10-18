"""Run finite-field cubic-surface census verification from this directory's parent."""
from pathlib import Path
import subprocess,json,collections,hashlib
root=Path(__file__).resolve().parent.parent
b=root/'replay_build';b.mkdir(exist_ok=True)
def run(cmd,log=None):
 p=subprocess.run(cmd,check=True,capture_output=True,text=True,cwd=root,timeout=180)
 if log:log.write_text(p.stdout)
 return p.stdout
for name in ('cubic_orbits','burnside'):
 run(['g++','-std=c++17','-O3',str(root/'code'/f'{name}.cpp'),'-o',str(b/name)])
assert run([str(b/'cubic_orbits')]) == (root/'data'/'orbits_all.txt').read_text()
assert run([str(b/'burnside')]) == (root/'data'/'burnside_output.txt').read_text()
run(['python3',str(root/'code'/'smooth_check.py'),str(root/'data'/'orbits_all.txt'),str(b/'smooth.json')])
assert json.loads((b/'smooth.json').read_text()) == json.loads((root/'data'/'smooth_classification.json').read_text())
run(['python3',str(root/'code'/'independent_contacts.py'),str(b/'smooth.json'),str(b/'contacts.json')])
assert json.loads((b/'contacts.json').read_text()) == json.loads((root/'data'/'independent_contacts.json').read_text())
run(['python3',str(root/'code'/'independent_lines.py'),str(b/'contacts.json')])
rows=json.loads((b/'contacts.json').read_text())
assert len(rows)==36 and sum(r['size'] for r in rows)==322560
hist=collections.Counter({})
for r in rows:hist[r['E']]+=r['size']
assert dict(hist)=={0:189952,1:115920,2:10080,3:2800,4:3360,7:420,15:28}
print('PASS: group orbits, Burnside, Groebner smoothness, symbolic tangent-contact classification, rational-line incidence. Smooth classes=36, equations=322560, Eckardt marginal=',dict(sorted(hist.items())))
