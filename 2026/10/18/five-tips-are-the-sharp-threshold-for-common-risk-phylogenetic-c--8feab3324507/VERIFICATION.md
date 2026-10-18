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
# Verification of the five-tip priority-switching theorem

The full mathematical argument is in `RESULT.md`, especially the root-split classification and factorized global-winner comparison. The finite executable checks below are additional reproducibility evidence, not a proof of the universal quantifier over all positive edge lengths.

Run `python3 verify.py` in the directory containing this file. It uses only Python's standard library and exact `fractions.Fraction` arithmetic, requiring no third-party packages or network access. It constructs a rooted eight-edge tree with tip set \(\{A,B,C,D,E\}\) and root-to-tip distance \(4\), with two-tip and three-tip crown stem lengths \(a=3\) and \(b=2\), and nested cherry stem endpoint \(t=3\). Its brute-force edge-set definition of rooted Faith PD is evaluated for each of the 16 possible sets of other survivors for each focal species. For five rational \(q\) values it compares these direct expectations with the independently implemented HED edge formula, including equality at \(q=1/2\) and strict winner reversals on either side.

The script also checks the exact score expressions, the polynomial identities \(\Psi_C-\Psi_A=(1-q)(1-2q)\) and \(\Psi_C-\Psi_D=(1-q)\), and the general \(2+3\) factorization in additional rational length examples, including boundary regimes. A successful run prints a line starting `VERIFY_OK`.

**Mathematical limits:** Rational tests sample finitely many \(q\) values and parameter instances. The universal statements for all \(q\in(0,1)\) and positive ultrametric lengths are established by exact analytic algebra in `RESULT.md`; no computer census, approximate roots, or external theorem-proving certification is substituted for that argument. The original HED branch formula is credited to Steel, Mimoto and Mooers (2007), and independent audit has not been performed.
