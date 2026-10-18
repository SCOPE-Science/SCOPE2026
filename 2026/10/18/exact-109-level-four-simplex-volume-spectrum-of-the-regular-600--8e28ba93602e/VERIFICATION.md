---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Verification

The exact code `verify_spectrum.cpp` enumerates every one of the \(\binom{119}{4}=7{,}940{,}751\) anchored vertex selections with integer-pair arithmetic in \(\mathbb Z[\varphi]\), where \(\varphi^2=\varphi+1\). It confirms the entire companion `spectrum.csv`, whose 109 rows sum to \(190{,}578{,}024\) quintuples. The source also repeats the complete enumeration from a different representative in each of the two remaining coordinate classes, and checks exact agreement.

From a shell in the same directory, run:

```sh
c++ -std=c++17 -O2 verify_spectrum.cpp -o verify_spectrum
./verify_spectrum --check spectrum.csv
python3 verify_examples.py
```

`verify_examples.py` uses SymPy for a separately computed exact determinant of two extremal configurations and their midpoint, proving that nonvertex equality configurations exist. These three commands completed successfully on the delivered sources. The C++ source also completed an undefined-behavior-sanitized build and run.

The table is the full vertex-supported distribution, not a distribution over all continuously chosen contained simplices. The code and table give an exact finite mathematical check, not independent auditing or general-purpose formal certification. Historical-priority assessment necessarily remains limited to the inspected sources.
