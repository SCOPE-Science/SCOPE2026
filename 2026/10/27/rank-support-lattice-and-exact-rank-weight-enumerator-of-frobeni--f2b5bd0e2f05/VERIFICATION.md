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

# Reproducibility and verification

Run `python verify_rank_profile.py` with a recent Python 3 interpreter and SymPy installed. The code needs no external files or network access. Its prime-base finite fields use explicit polynomial residues, with exhaustive nonzero inverse testing; ranks are computed by modular row reduction and actual distinct field-coordinate spans are represented by canonical reduced row-echelon bases. For cyclic groups it enumerates *every* independent Frobenius-orbit seed tuple and compares to the independent irreducible-factor enumerator.

The six full cyclic tests have \((q,m,n)=(2,2,3),(2,3,7),(2,4,5),(2,4,15),(3,2,8),(5,2,6)\), encompassing \(8+128+32+32768+6561+15625=55122\) complete spectral codewords. The output file `verify_output.txt` records distributions, counts of distinct observed rank-support subspaces, and `RANK_PROFILE_VERIFY_OK`.

An independent direct Fourier-transform test on the noncyclic group \(C_3\times C_3\) over \(\mathbb F_2\), into \(\mathbb F_4\), checks all 512 input functions without using the seed-space construction. Its rank distribution is \(1+31z+480z^2\), with exactly three rank-support subspaces, and it emits `NONCYCLIC_DFT_VERIFY_OK`.

This executable checks small prime-base examples only, not arbitrary nonprime base fields or an infinite family. The general conclusions rely on the explicit proof in `RESULT.md`: Fourier descent, normal-basis cyclicity, the least-common-multiple submodule identity, CRT count, and existence of a maximal-length character orbit. No independent audit is claimed.
