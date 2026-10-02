exec(open('artifacts/h5_quotient.py',encoding='utf-8').read().split("for k in [4,5,6]:")[0])
for k in [7]:
    print("="*60, flush=True)
    print(compute_H5(k), flush=True)

