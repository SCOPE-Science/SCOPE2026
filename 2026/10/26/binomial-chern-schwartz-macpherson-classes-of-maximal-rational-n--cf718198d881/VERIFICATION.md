---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-31.md",
      "INDEPENDENT_AUDIT_2026-10-31.json"
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

Let n=2r and let S_s be the binary-form border-rank <=s locus. For each s<=r, the apolar contraction map from degree-n forms to degree-(n-s) forms twisted by the degree-s operator line is surjective because multiplication by a nonzero binary form is injective on the dual side. Its rank-s kernel E_s defines a smooth projective incidence B_s=P(E_s), dimension 2s-1, cut out by n-s+1 regular bilinear equations. The standard apolar ideal of a binary form in T_l=S_l\S_(l-1) has least generator degree l and its second generator degree n+2-l, so for s<=r the degree-s annihilators form P^(s-l). Their Euler characteristic s-l+1 gives pi_s*1_B_s=sum_(l<=s)1_S_l. Thus 1_S_r=pi_r*1_B_r-pi_(r-1)*1_B_(r-1). Proper CSM pushforward and regular-section adjunction give the exact coefficient [h^s](1+h)^(s+1)(1+H)^(2r+1)((h+H)/(1+h+H))^(2r-s+1). Algebraically summing the two adjacent incidence terms using formal diagonal/Lagrange extraction yields the stated square-root generating function. An independent constant-term derivation yields the same series and binomial coefficients binom(r,floor i/2)binom(r,ceil i/2) for every r, i. The Aluffi triangular class/gradient-degree relation then proves polynomiality in r with degree<=i, so both parts of Nogueira Conjecture 4.1 follow. Independently expanded the complete truncated bivariate incidence class in exact integer arithmetic for r=1..7, reproducing all 63 coefficient patterns, but this bounded test cannot replace the formal all-r proof. The r=1 conic complement and Euler characteristic are consistent.

## originality

PASS

Nogueira 2020 thesis / arXiv:2309.09254 Section 4 Conjecture 4.1 and Theorem 4.11 expressly CONJECTURE the identical binomial CSM formula as an equivalent statement; the thesis gives finite evidence but not the all-r proof. Brogan arXiv:2408.16736 provides general secant incidence fiber geometry for positive embeddings but works on intersection cohomology and vanishing cycles; the necessary fiber geometry is PRIOR, not new. Aluffi CSM functoriality/polar transformations are established inputs. A more general CSM determinantal formula potentially implies this specialization and is retained as an originality risk. Best-of-knowledge novelty assessment of the surviving precise mathematical contribution; unsuccessful database search is not proof of absolute priority.

## value

PASS

The theorem resolves the explicitly formulated all-r polynomiality conjecture for maximal secant hypersurface complements of even-degree rational normal curves, giving a compact closed CSM class and the associated full polar-degree consequences. The incidence-fiber calculation and generating-function evaluation are mathematically substantive and useful far beyond the verified finite r cases, without claiming all arbitrary secant varieties.

The dated certificate retains the supplied scientific assessment, sources and limitations.
