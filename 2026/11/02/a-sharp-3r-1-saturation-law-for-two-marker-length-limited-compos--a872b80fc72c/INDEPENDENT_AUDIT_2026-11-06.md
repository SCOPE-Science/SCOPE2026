# Independent mathematical audit

## correctness

PASS

For binary linear 0^a 1 0^b 1 0^c, the known n and counts N_{ell,j} give polynomials F and G. Multiplication by (1-z)^2 yields exact identities 2z-z^(a+2)-z^(b+2)-z^(c+2)+z^(n+2) and z^(b+2)-z^(a+b+3)-z^(b+c+3)+z^(n+2). Truncation through r recovers B=b+2 exactly if B<=r, and the multiset of outer markers A=a+1,D=c+1 below r, while all other information is invisible. The iff profile-signature classification follows both directions. Counting unordered A,D by visible B, both-small, exactly-one-small, neither-small gives four displayed terms. For n>=3r-1 they are r(r-1),r(r-1)/2,r-1,1, totaling r(3r-1)/2; one-class deficit at n=3r-2 (r>=2); r=1 is correctly handled. Independent literal substring profiles and both-way signature tests confirm every n<=18, all r<=n; formula boundary checked to r=59. Full proof not inferred from testing.

## originality

PASS

The r-dependent exactly-two-marker profile equivalence and sharp stabilization differ from known full-deck reconstruction or restricted length-r code constructions. Existing published all-weights r=2 exact enumeration naturally covers an r=2 special case, but not the uniform-in-r classification. Priority qualification remains for sparse reconstruction/turnpike specializations.

## value

PASS

Substring-composition channels are natural in polymer/string reconstruction; the result supplies an exact maximum zero-error code size and a full ambiguity-fiber classification with a sharp observation-length saturation boundary. It quantifies what length-limited reads can and cannot distinguish rather than merely tabulating small n.

The dated certificate retains the supplied scientific assessment, sources and limitations.
