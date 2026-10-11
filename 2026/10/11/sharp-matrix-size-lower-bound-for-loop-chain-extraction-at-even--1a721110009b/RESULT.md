# Sharp matrix-size lower bound for loop-chain extraction at even exponents

## Finding

For every integer \(m\ge 2\), put \(r=2m-1\). A **loop-chain encoding** of length \(r\) in \(\mathrm M_n\) is a labeled family \(F_1,\ldots,F_r\) of matrix units satisfying all of the following:

- every \(F_k\) is either a loop \(E_{s,s}\) or a forward edge \(E_{s,s+1}\);
- for each \(1\le s<n\), the forward edge \(E_{s,s+1}\) occurs exactly once;
- there are no other nonloop edges;
- the identity ordering is composable from vertex \(1\) to vertex \(n\), so \(F_1\cdots F_r=E_{1,n}\).

Call such an encoding **parity-isolating** when the identity is the only permutation \(\pi\) of \(\{1,\ldots,r\}\) satisfying \(\pi(j)\equiv j\pmod 2\) for every \(j\) and
\[
(F_{\pi(1)}\cdots F_{\pi(r)})_{1,n}\ne0.
\]

Every parity-isolating loop-chain encoding satisfies
\[
n\ge \left\lceil\frac{2m}{3}\right\rceil.
\]
The matrix-unit choice in the proof of Theorem 7.1 of Arhancet, arXiv:2610.03375v1, attains equality. Thus its level \(N_m=\lceil2m/3\rceil\) is optimal within this loop-chain, single-entry, parity-Fourier extraction architecture.

## Assumptions and scope

The statement is purely combinatorial after the alternating word length \(r=2m-1\) has been fixed. The parity condition is exactly the one produced by the torus Fourier coefficient in the source: surviving monomials are indexed by permutations preserving odd and even label classes.

The conclusion concerns only encodings with one copy of each forward edge \(E_{s,s+1}\) and all remaining labeled matrix units loops. It does not assert that \(N_m\) is the optimal matrix level among all proofs of complete contractivity.

## Proof

Fix a parity-isolating loop-chain encoding in \(\mathrm M_n\). There are exactly \(n-1\) nonloop labels, one for each forward edge \(E_{s,s+1}\). Therefore the number of loop labels is
\[
r-(n-1).
\]

No vertex can carry three loop labels. Indeed, if three labels \(a,b,c\) all represent the same loop \(E_{s,s}\), two of \(a,b,c\) have the same parity. Call them \(a\) and \(b\). Let \(\pi\) swap \(a\) and \(b\) and fix every other label. Since \(a\equiv b\pmod2\), this \(\pi\) is parity-preserving. But \(F_a=F_b=E_{s,s}\), so swapping the two labels leaves the matrix-unit product unchanged:
\[
F_{\pi(1)}\cdots F_{\pi(r)}=F_1\cdots F_r=E_{1,n}.
\]
This contradicts parity isolation. Hence there are at most two loop labels at each of the \(n\) vertices.

Consequently
\[
r-(n-1)\le 2n.
\]
Since \(r=2m-1\), this gives
\[
2m=r+1\le3n,
\]
and therefore
\[
n\ge\left\lceil\frac{2m}{3}\right\rceil.
\]

For sharpness within this architecture, the source sets
\[
v_k=1+\left\lfloor\frac{k}{3}\right\rfloor,\qquad
F_k=E_{v_{k-1},v_k},\qquad 1\le k\le2m-1.
\]
Then \(v_0=1\) and
\[
v_{2m-1}=1+\left\lfloor\frac{2m-1}{3}\right\rfloor
=\left\lceil\frac{2m}{3}\right\rceil.
\]
The source proves that every interior stage has two loops followed by the forward edge, with at most two terminal loops, and that parity preservation forbids the only possible loop interchange. Hence the identity is the unique parity-preserving ordering with nonzero selected entry, so equality is attained.

## Verification

The focal source was checked at its introduction and Section 7. It defines \(N_m=\lceil2m/3\rceil\), states that this level is sufficient without claiming global optimality, and in the proof of Theorem 7.1 uses the labels \(v_k=1+\lfloor k/3\rfloor\) and the matrix units \(F_k=E_{v_{k-1},v_k}\). Its torus coefficient leaves exactly parity-preserving permutations, and its path argument proves uniqueness of the identity ordering for the selected \((1,N_m)\)-entry.

The new lower bound uses only the equality of loop matrix units at a fixed vertex, parity preservation, and the exact count of forward edges. No numerical experiment, finite enumeration, or unproved limiting argument is used.

## Relationship to prior work

Arhancet proves that \(N_m=\lceil2m/3\rceil\)-contractivity implies complete contractivity for projections on noncommutative \(\mathrm L^{2m}\)-spaces and explicitly says that the displayed level is not claimed to be globally optimal. The present statement does not strengthen that theorem to a global lower bound. Instead, it proves that the matrix size in the source cannot be reduced by repacking the same loop-chain and single-entry Fourier-isolation mechanism.

The source also recalls that, for Schatten spaces, earlier work of Le Merdy, Ricard and Roydor gives level \(2\) sufficiency for every non-Hilbert exponent. That special-ambient result is compatible with the present claim because it uses different structural information and does not imply a smaller parity-isolating loop-chain encoding.

Targeted database searches for the source identifier, the value \(\lceil2m/3\rceil\), parity-preserving matrix-unit paths, loop-chain extraction, and method optimality found no statement equivalent to this architecture-specific lower bound.

## Limitations

The result does not prove that \(\lceil2m/3\rceil\) is the globally minimal matrix level for arbitrary von Neumann algebras. It does not rule out encodings using different matrix-unit graphs, repeated or skipped forward transitions, several selected entries, cancellations among Fourier coefficients, or a proof not based on this path-isolation device. An older equivalent observation may exist under combinatorial path-ordering terminology; no such source was found in the searches performed.

## References

1. Cédric Arhancet, *A modular theory of contractive projections on Banach spaces with applications to noncommutative \(\mathrm L^p\)-spaces*, arXiv:2610.03375v1, 2026.
2. Christian Le Merdy, Éric Ricard, and Jean Roydor, *Completely 1-complemented subspaces of Schatten spaces*, Transactions of the American Mathematical Society 361 (2009), 849–887.
