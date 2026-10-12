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
The packaged `verify.py` uses exact symbolic arithmetic to check the complete projective-stabilizer computation for
\[
S_a=\{0,1,-1,a,-a\},\qquad a\ne0,\pm1.
\]
It performs these checks:

1. Enumerates all \(120\) permutations of the five marked points.
2. For each permutation, compares two independent cross-ratios exactly; this is necessary and sufficient for extension to a Möbius transformation because three distinct point images determine that transformation.
3. Removes only the excluded collision factors \(a\), \(a-1\), and \(a+1\).
4. Confirms that the only remaining exceptional factors are \(a^2+1\), \(a^2+3\), \(3a^2+1\), \(a^2-4a-1\), and \(a^2+4a-1\).
5. Counts the resulting stabilizers as orders \(4,6,6,10,10\), with order \(2\) away from these loci.

The script proves the finite classification by exhaustive exact identities; it is not a numerical sampling argument. Group identification from these orders uses the standard orbit structure of finite subgroups of \(\operatorname{PGL}_2(\mathbb C)\), as explained in `RESULT.md`.

No claim is made about descent of these automorphisms to a nonclosed field.
