exec(open('output/artifacts/h5_quotient.py').read().split("for k in [4,5,6]:")[0])
for k in [7]:
    print("="*60, flush=True)
    print(compute_H5(k), flush=True)
