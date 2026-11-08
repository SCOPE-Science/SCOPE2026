---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-07.md",
      "INDEPENDENT_AUDIT_2026-11-07.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

The final recurrence B_1=101, B_{i+1}=B_i B_i[i+1..|B_i|], and length 2^{i-1}+i+1 fix all normalization conventions. For a fixed length-m cylinder, whole-factor counts satisfy N_{i+1}=2N_i-D_i+J_i with 0<=D_i<=i and 0<=J_i<=m-1; summing scaled errors proves N_i=2^{i-1}mu+O(i+m). Comparing arbitrary prefixes to a shorter initial index (contracting by <=3/4) bounds the accumulated discrepancy by O_u((1+log N)^2). A factor occurring arbitrarily late has doubling descendants until its starting index p, overwhelming the eventual loss budget p+1; this proves strict positive frequency for every allowed factor, with forbidden 00 absent. To prove h_mu=0 the recursion embeds B_I as a subsequence of B_j^{2^{I-j}}, deleting 2^{I-j}(j+1)-I-1 symbols; at most m times this count damages length-m windows. Thus H_m<=1+log_2|B_j|+m min(1,m(j+1)/2^{j-1}); m=2^{floor(j/2)} makes H_m/m tend to zero. Subadditivity makes the full entropy rate zero. Recurrent/full-language input from Shallit is explicitly assumed; not derived from computer checks. Independent finite reconstruction through level16 agrees with length, no-00 and factor-frequency behavior, not an infinite proof.

## originality

PASS

Best-of-knowledge PASS. Shallit's original Brik-word paper identifies the same sequence, exact recursive lengths, recurrence, language avoiding 00, and single-letter frequency; those facts do not imply limits/positivity for every cylinder nor the entropy of that empirical invariant measure. The new all-cylinder logarithmic-square discrepancy and full-support zero-entropy law are additional assertions. Rank-one and finite-symbolic-rank techniques are contextual; general existence of zero-entropy full-support measures is not a computation of this sequence's empirical frequencies.

## value

PASS

Natural invariant measure induced by a specifically studied recursive word, with a meaningful paradox: its orbit closure has exponential Fibonacci block growth and positive topological entropy while its actual cylinder-frequency measure is fully supported and has zero metric entropy. Existence, positivity and quantified all-cylinder discrepancy go substantially beyond its known one-letter density; this is a structural statement usable in symbolic-dynamics questions, not a routine factor count.

The dated certificate retains the supplied scientific assessment, sources and limitations.
