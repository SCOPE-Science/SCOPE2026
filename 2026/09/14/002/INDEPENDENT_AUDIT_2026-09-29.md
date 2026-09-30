# Independent audit — 2026-09-29

Record: `2026/09/14/002`  
Audited source tree: `79aeffdd82402874c92ed439773a4d5d0df4ad93`  
Disposition: **passed**

## Correctness

The truncation geometry follows directly from the multilinearized relations. For a last visible point c=(c0:c1:c2), the extension fiber is the projectivized kernel of M(c)=[[c0,0,0],[0,c1,0],[c2,c2,0]]. Its third column is identically zero, giving the global section [0:0:1] and hence surjectivity. Because c is projective and nonzero, rank M(c) is 1 or 2, so every scheme-theoretic geometric fiber is P^1 or P^0 and is connected. At P=([0:0:1])^3, eliminating the two linear equations in the affine chart leaves the ideal x1(x0,y0,x2), the union of A^3 and A^1 meeting at the origin; the Jacobian rank is two and the tangent dimension is four, so P is singular. The archived SymPy checks are consistent with these direct calculations.

## Originality

General truncated point-scheme and flat-family theory is established. A focused search did not identify this exact degenerate relation space and fiber calculation in the accessible literature. The result is therefore best characterized as an explicit worked case, not a general theorem or a proven priority claim.

## Scientific value

The record gives a complete and elementary description of the relevant truncation map and a concrete singularity certificate. Its value is in resolving the named exceptional presentation exactly; it does not generalize the result to other exceptional-divisor algebras.

## Limitations

- The identification of the explicit presentation with the named Hwang exceptional-divisor example is taken from the record's admitted topic fingerprint and was not independently established from an accessible thesis text.
- The statement is specific to E=k<x,y,z>/(x^2,y^2,zx+zy) over algebraically closed characteristic not 2 or 3.
- The ancillary count of monomial relation lines is a statement in the displayed coordinate presentation and should not be read as a coordinate-free classification under arbitrary changes of generators.
- RESULT.md and METADATA.json refer to output/artifacts/verify.py, while the audited repository stores the script at artifacts/verify.py; this packaging path mismatch does not affect the mathematics.
- Literature search non-detection is not proof of novelty or priority.

## Sources checked

- https://github.com/SCOPE-Science/SCOPE2026/tree/e9ed144c13b7834896a844cc4f9cac3c25a168a6/2026/09/14/002
- https://arxiv.org/abs/1709.08757
