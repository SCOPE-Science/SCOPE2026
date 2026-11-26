---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

Write U for the common product image and P,Q for the separate images of A,B. Since B(P)=U and its kernel on P contains U, dim P>=2r, and symmetrically dim Q>=2r. Square-zero gives the opposite bounds and P=ker A, Q=ker B. Now ker(B|P)=P intersect Q=U, and both products kill P+Q, a 3r-space, so their kernels are exactly that space. Choose W complementary to P+Q. Then A(W),B(W) complement U in P,Q, and AB:W→U is an isomorphism. Transferring a basis of W gives the displayed matrices with H=(AB)^{-1}BA on the quotient; change of basis acts by similarity. Commutation determines the other columns from the W column (R,S,T,P0): they are (P0,0,0,0), (T,P0,0,0) and (HS,0,P0,0). The only constraint is P0H=HP0, and invertibility is exactly that of P0. Summing the orbit counts over invertible similarity classes uses the GL_r class equation. Independently, with A fixed, choose U in P of dimension r, then Q/U complementary to P/U in A^{-1}(U)/U: the respective counts are Gaussian(2r,r) and q^{r²}. Choose the isomorphism V/Q→Q inducing B and sending (P+Q)/Q onto U, giving q^{r²}|GL_r|² choices. The product is q^{r²}|GL_{2r}|, as claimed. These arguments are characteristic-free and give the stated 2520 and 898560. The frozen small-field and centralizer checks were inspected, not run.

## originality

PASS

The supported claim is the finite-field mass of the equal-product-image sharp stratum without commutativity, with the accompanying explicit normal form and simultaneous centralizer. Neither the bound, the commuting orbit and its binary r=1 specialization, nor general string/band classification is credited as new.

## value

PASS

The natural locus is the equality case of a known rank bound. Counting labeled realizations, including the noncommuting pairs, quantifies a refinement that rank strata do not capture. The exact class and stabilizer description explains the simple aggregate mass uniformly across characteristics.

The dated certificate retains the supplied scientific assessment, sources and limitations.
