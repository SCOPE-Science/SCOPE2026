import json
from pathlib import Path
p=Path(__file__).with_name('witness_5.json')
q=json.loads(p.read_text())
assert len(q['colorings_by_binary_word'])==32
for bits,c in q['colorings_by_binary_word'].items():
 assert len(bits)==5 and len(c)==7
 assert all(c[u]!=c[v] for u,v in q['edges'])
 assert bits==''.join(str(int(c[u]==a)) for u,a in zip(q['queried_vertices'],q['queried_colors']))
print('ALL_32_VC5_WITNESSES_PASS')
