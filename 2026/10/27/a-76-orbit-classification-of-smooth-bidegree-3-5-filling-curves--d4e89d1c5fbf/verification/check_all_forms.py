"""Independent exhaustive check on every rationally smooth equation, without orbit pruning."""
import runpy,time,collections
from pathlib import Path
root=Path('.')
b=runpy.run_path(str(root/'independent_basis.py'))
g=runpy.run_path(str(root/'check_groebner.py'))
valid=b['smooth'];ck=g['is_smooth'];t=time.monotonic();smooth=[v for v in valid if ck(v)]
print('All-form independent exact singular-ideal classification:',len(smooth),'out of',len(valid),'rational-smooth forms; elapsed',round(time.monotonic()-t,2),flush=True)
assert len(smooth)==2304
import json
with open(root/'independent_all_form_counts.json','w') as f:json.dump({'total_filling_forms':32768,'rationally_smooth':len(valid),'geometrically_smooth':len(smooth),'complete':True},f)
