"""Verify every archived matrix. Requires Python 3 and gcc, no network."""
import subprocess,tempfile
from pathlib import Path
root=Path(__file__).resolve().parent
files=sorted((root/'gs_designs').glob('gsdes18_*.txt'))
assert len(files)==1458
seen=set();lines=['1458']
for file in files:
    values=tuple(map(int,file.read_text().split()))
    assert len(values)==1296 and set(values)<={0,1}
    assert values not in seen;seen.add(values)
    lines.extend([file.name,' '.join(map(str,values))])
with tempfile.TemporaryDirectory(prefix='design-certificate-') as temp:
    temp=Path(temp);binary=temp/'verify';packet=temp/'input.txt'
    packet.write_text('\n'.join(lines)+'\n')
    subprocess.run(['gcc','-O3','-std=c11',str(root/'verify_maintenance.c'),'-o',str(binary)],check=True)
    with packet.open('rb') as data:
        subprocess.run([str(binary)],stdin=data,check=True)
