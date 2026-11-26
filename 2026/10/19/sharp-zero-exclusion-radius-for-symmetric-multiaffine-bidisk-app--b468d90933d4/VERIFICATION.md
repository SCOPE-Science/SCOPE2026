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

Uniqueness under the weighted Hilbert norm and swap symmetry reduce the affine approximant to A+B M, M=z₁+z₂. The Mf equation forces B=0 if A=0, contradicting the other equation since u≠0. Expanding Mf gives 2v|u|²+(2w+4v²)|a|²+2vw|b|² for its squared norm and cross-term magnitude 2v|uȧ+vab̄|, where ȧ denotes conjugation of a. Thus 2|B/A| is bounded by the generalized Rayleigh quotient with Q off-diagonals 1,v and D=diag(1,w/v+2v,w). The top eigenvalue of D^{-1/2}QD^{-1/2} is simple and equals ηα. Clarifying the shorthand in line 49, the displayed (1,ηα,v/w) is the generalized eigenvector in the original variables, satisfying QX=ηαDX; the ordinary eigenvector of the conjugated matrix is D^{1/2}X. Phase alignment gives exactly the stated equality family. The diagonal attains the triangle-inequality lower bound |A/(2B)| on zero radius (no zeros if B=0). For α>0, h=v/w<1 and 2ηα<1+h make the boundary squared-modulus difference (1−h)(1+h+2ηα Re z) strictly positive; the maximum-modulus argument rules out all closed-bidisk zeros of the generator. At α=0 the extremal generator can have boundary zeros, which is outside that sharpness subclaim. The identity ηα²=h(1+t)/(1+2t), t=(4/3)^α, proves all monotonicity and limit assertions. The exact algebra, not the finite tests, proves the theorem.

## originality

PASS

The diagonal criterion and projection method are established techniques, and earlier counterexamples use the same notion of an affine approximant. The strongest matched sources concern other generator families or larger degrees. Neither their extremizers nor their conclusions give the all-α sharp radius and phase-rigid family for all symmetric multiaffine generators, including closed-bidisk zero-free sharpness for α>0.

## value

PASS

This gives the exact positive safety margin in a natural low-degree symmetric bidisk class within a problem where higher-degree generators allow interior approximant zeros. It also explains equality, shows why restricting to zero-free generators for positive weights does not improve the sharp margin, and quantifies how the margin depends on the Dirichlet exponent. This is more than verifying zero exclusion or a particular example.

The dated certificate retains the supplied scientific assessment, sources and limitations.
