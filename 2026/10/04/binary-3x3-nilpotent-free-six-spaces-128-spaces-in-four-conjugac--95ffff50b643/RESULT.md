# Binary 3x3 nilpotent-free six-spaces: 128 spaces in four conjugacy orbits

## Finding
In \(M_3(\mathbb F_2)\), there are exactly \(128\) six-dimensional linear subspaces containing no nonzero nilpotent matrix. Under conjugation by \(\mathrm{GL}_3(\mathbb F_2)\), these \(128\) spaces split into four orbits of sizes \(8,8,56,56\).

A concrete example is
\[
W=\left\{\begin{pmatrix}
a&b&c\\
a+b&d&e\\
a+c+e&b+d+e&f
\end{pmatrix}:a,b,c,d,e,f\in\mathbb F_2\right\}.
\]
Thus \(\dim W=6=3^2-\binom32\), and \(W\) contains no nonzero nilpotent matrix. Consequently Conjecture 8 of Wigderson holds for \((F,n)=(\mathbb F_2,3)\).

## Assumptions and scope
All matrices and vector spaces are over \(\mathbb F_2\). Nilpotent means nilpotent as a \(3\times3\) endomorphism; equivalently, for this size, \(A^3=0\). The conjugacy action is \(W\mapsto gWg^{-1}\) for \(g\in\mathrm{GL}_3(\mathbb F_2)\).

The exact census concerns linear six-spaces in the nine-dimensional vector space \(M_3(\mathbb F_2)\). It does not assert an analogous count for other finite fields or larger matrix sizes.

## Proof
The displayed parametrization is injective in the six parameters \(a,b,c,d,e,f\), so \(W\) has \(2^6\) elements and dimension \(6\). Equivalently, it is the common kernel of the three independent linear forms
\[
x_{11}+x_{12}+x_{21},\qquad
x_{11}+x_{13}+x_{23}+x_{31},\qquad
x_{12}+x_{22}+x_{23}+x_{32}.
\]

There are only \(2^9=512\) matrices in \(M_3(\mathbb F_2)\). Direct exact multiplication shows that exactly \(64\) satisfy \(A^3=0\), including zero. Exhausting the \(64\) matrices in the displayed \(W\) shows that its intersection with those \(63\) nonzero nilpotents is empty. Hence \(W\) is a six-dimensional nilpotent-free space.

For the census, every six-dimensional subspace of \(\mathbb F_2^9\) has a unique reduced-row-echelon basis. Enumerating those bases gives exactly
\[
{9\brack6}_2={9\brack3}_2=788035
\]
six-spaces. Testing each space against the complete set of \(63\) nonzero nilpotent matrices yields exactly \(128\) nilpotent-free six-spaces.

A second enumeration reaches the same set from orthogonal complements. With the entrywise pairing \(\langle X,Y\rangle=\sum_{i,j}x_{ij}y_{ij}\), a six-space \(W=U^\perp\) is nilpotent-free exactly when every nonzero nilpotent \(N\) has \(\langle N,u\rangle=1\) for at least one \(u\in U\). Enumerating all \({9\brack3}_2=788035\) three-spaces \(U\) gives the same \(128\) kernels.

Finally, \(|\mathrm{GL}_3(\mathbb F_2)|=168\). Exact conjugation of the \(128\) spaces partitions them into four orbits with sizes \(8,8,56,56\). The displayed space belongs to one of the size-\(56\) orbits.

## Verification
The standalone file `verify.py` performs two independent exhaustive censuses: direct enumeration of all six-spaces and enumeration through three-dimensional orthogonal complements. It also independently enumerates all \(168\) invertible binary \(3\times3\) matrices and computes the conjugacy orbits. Its terminal certificate is `VERIFY_OK` together with the counts \(64\), \(788035\), \(128\), and orbit sizes \(8,8,56,56\).

All arithmetic is exact bit arithmetic over \(\mathbb F_2\); there is no randomized step or floating-point computation.

## Relationship to prior work
Wigderson's 2026 paper observes that the Gerstenhaber--Serezhkin theorem would admit the same duality strategy if, over every finite field, one could exhibit a subspace of dimension \(n^2-\binom n2\) containing no nonzero nilpotent. The paper states that such a construction is straightforward over \(\mathbb R\) using symmetric matrices, but that over finite fields it is not clear whether it is even true, and formulates this as Conjecture 8.

The present result gives the next binary case after \(n=2\): it supplies an explicit six-dimensional witness for \(M_3(\mathbb F_2)\) and, more strongly, the complete binary census and conjugacy-orbit decomposition. The classical Gerstenhaber--Serezhkin literature classifies large spaces consisting of nilpotent matrices; that result is the extremal theorem being dualized and does not itself supply a complementary nilpotent-free six-space.

## Limitations
The proof is a finite exhaustive proof specialized to \(M_3(\mathbb F_2)\). It gives neither a conceptual construction valid for all \(q\) or \(n\), nor a proof of Conjecture 8 beyond this parameter pair. The literature search found no source stating the explicit witness, the count \(128\), or the orbit sizes \(8,8,56,56\), but an older or differently phrased finite-geometry classification could still encode an equivalent small-case result.

## References
1. Yuval Wigderson, *Duality for matrix space questions*, arXiv:2609.29177v1, submitted 24 September 2026. In particular, Conjecture 8 asks for \(n^2-\binom n2\)-dimensional nilpotent-free matrix spaces over finite fields.
2. Clément de Seguins Pazzis, *On Gerstenhaber's theorem for spaces of nilpotent matrices over a skew field*, arXiv:1210.4951v2; Linear Algebra Appl. 438 (2013), 4426--4438. This gives the nilpotent-space extremal background, not the dual nilpotent-free construction above.
