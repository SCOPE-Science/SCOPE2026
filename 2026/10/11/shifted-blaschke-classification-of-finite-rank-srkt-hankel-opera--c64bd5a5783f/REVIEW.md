# Review of Shifted-Blaschke classification of finite-rank SRKT Hankel operators

## Correctness

PASS. Finite rank makes the operator compact, so the kernel-testing function tends to zero at the boundary and an SRKT operator has an interior norming kernel. Kronecker rationality makes the symbol bounded. Moving that kernel to zero by a disk automorphism preserves the quotient norm, while harmonic measure turns the tested kernel norm into the \(L^2\) norm of the transformed symbol. The transformed symbol therefore has minimal Hankel norm.

The checked minimal-norm theorem forces maximal norm, so the transformed rational symbol has constant boundary modulus and is a constant multiple of a finite Blaschke product. Undoing the automorphism and imposing the normalization at zero gives exactly
\[
\psi=C(B-B(0)).
\]

Conversely, the Bonsall identity gives
\[
\|H_{\overline\psi}k_a\|_2^2
=
|C|^2(1-|B(a)|^2).
\]
At a zero of \(B\) this reaches \(|C|\), while the quotient-distance estimate gives \(\|\psi\|_*\le|C|\). Hence all inequalities collapse to equality. The kernel of \(H_{\overline B}\) is \(BH^2\), giving rank \(\deg B\). Every displayed conclusion follows exactly.

## Originality

PASS. The fresh paper formulates the full SRKT equality problem and asks explicitly for bounded examples with strict separation from the uniform norm, but it does not identify shifted finite Blaschke products or classify finite-rank symbols.

The closest existing completed result classifies only polynomial symbols, where monomials are forced. The present theorem strictly extends that statement to all finite-rank rational symbols and gives the exact set of norming reproducing kernels.

Kronecker's theorem supplies rationality only. Minimal-norm Hankel theory supplies the inner-function conclusion only after a different equality has been established. General norm-attainment theory describes norm-achieved Hankel operators but does not state which reproducing kernels can achieve the norm. Targeted source, alias, and implication searches did not locate the shifted-Blaschke classification.

## Value

PASS. Finite rank is the first natural nontrivial structural class for the open SRKT problem, and a complete classification is mathematically more informative than an isolated example. The theorem also resolves the fresh paper's explicit bounded-example request by a transparent rank-one family and explains exactly when the strict uniform-norm gap occurs.

The additional formula
\[
\|H_{\overline\psi}k_a\|_2^2
=
|C|^2(1-|B(a)|^2)
\]
identifies the entire norming-kernel locus and turns the classification into a reusable geometric description rather than a normalization trick.

Same-model review: passed. Independent audit: not yet performed.
