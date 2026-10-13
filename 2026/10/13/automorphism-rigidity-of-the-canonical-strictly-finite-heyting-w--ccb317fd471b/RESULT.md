# Automorphism rigidity of the canonical strictly finite Heyting witnesses

## Finding
For every integer \(n<\omega\), let \(X_n\) be the canonical Esakia space introduced in the strict-finiteness construction of Hyttinen, Martins, Moraschini, and Quadrellaro, and let
\[
H_n=X_n^*
\]
be its dual Heyting algebra. Then the underlying poset of \(X_n\) is rigid. In particular,
\[
\boxed{\operatorname{Aut}_{\mathrm{Esakia}}(X_n)=\{1\}}
\qquad\text{and}\qquad
\boxed{\operatorname{Aut}_{\mathrm{Heyt}}(H_n)=\{1\}}.
\]
This holds uniformly for every \(n\ge0\), including the endpoint \(n=0\), where the source identifies \(X_0^*\) with the Rieger--Nishimura free one-generated Heyting algebra.

## Source setting
Definition 4.1 of the source writes
\[
X_n=\{x_i^l: l\le 2^n,\ i<\omega\}\cup\{x_\infty\}
\]
with minimum \(x_\infty\), levels
\[
L_n^i=\{x_i^l:l\le2^n\},
\]
and, between distinct finite-level points,
\[
x_i^l\le x_{i'}^{l'}
\quad\Longleftrightarrow\quad
 i\ge i'+2\ \text{ or }\ \bigl(i=i'+1\text{ and }l'\ne l+1\bigr).
\]
The article uses these spaces to obtain infinite \((n+1)\)-generated Heyting algebras whose \(n\)-generated subalgebras are uniformly finite.

Put \(m=2^n\), so every finite level has \(m+1\) points.

## Proof
### 1. Every level is order-theoretically fixed
The point \(x_\infty\) is the unique minimum, hence is fixed by every order automorphism. The maximal elements of \(X_n\) are exactly \(L_n^0\). After deleting \(L_n^0\), the maximal elements of the remainder are exactly \(L_n^1\); continuing recursively, after deleting \(L_n^0,\dots,L_n^{i-1}\), the maximal elements are exactly \(L_n^i\). Therefore every order automorphism preserves each level setwise.

### 2. The zero-labelled point on each level is intrinsic
Fix \(i<\omega\). For a lower point \(x_{i+1}^l\) and an upper point \(x_i^u\), the adjacent-level relation is
\[
x_{i+1}^l\le x_i^u\quad\Longleftrightarrow\quad u\ne l+1.
\]
Hence \(x_i^0\) lies above every point of \(L_n^{i+1}\): the forbidden value \(l+1\) is always at least \(1\). Conversely, if \(u>0\), then \(x_{i+1}^{u-1}\not\le x_i^u\). Thus
\[
\boxed{x_i^0\text{ is the unique point of }L_n^i\text{ above all of }L_n^{i+1}.}
\]
Every order automorphism therefore fixes \(x_i^0\) for every \(i\).

Dually within the same adjacent-level incidence graph, \(x_{i+1}^{m}\) is the unique point of \(L_n^{i+1}\) lying below every point of \(L_n^i\), because its forbidden upper label would be \(m+1\), which is absent.

### 3. The missing-upper map intrinsically recovers every label
For \(l<m\), the lower point \(x_{i+1}^l\) fails to lie below exactly one point of \(L_n^i\), namely \(x_i^{l+1}\). Therefore the order alone defines a bijection
\[
s_i:L_n^{i+1}\setminus\{x_{i+1}^{m}\}
\longrightarrow
L_n^i\setminus\{x_i^0\},
\qquad
s_i(x_{i+1}^l)=x_i^{l+1}.
\]
Because \(s_i\) is defined solely from the order relation, every order automorphism commutes with it.

For each \(k=1,\dots,m\), iterating these intrinsic maps gives
\[
x_i^k
=s_i\,s_{i+1}\cdots s_{i+k-1}(x_{i+k}^0).
\]
The point on the right is fixed: \(x_{i+k}^0\) is fixed by Step 2, and each \(s_j\) is automorphism-equivariant. Thus every \(x_i^k\) is fixed. Together with \(x_i^0\) and \(x_\infty\), every point of \(X_n\) is fixed. Hence the underlying poset has trivial automorphism group.

### 4. Transfer to the Heyting algebra
An Esakia automorphism is in particular an order automorphism, so it must be the identity. Section 2 of the source recalls that Esakia duality is a dual categorical equivalence between Heyting algebras with homomorphisms and Esakia spaces with Esakia morphisms. Therefore a Heyting automorphism of \(X_n^*\) dualizes to an Esakia automorphism of \(X_n\). Since the latter is trivial, so is
\[
\operatorname{Aut}_{\mathrm{Heyt}}(X_n^*).
\]

## Why this is not implied by the earlier monogenic-spectrum findings
Earlier owned findings determined the sizes and multiplicities of one-generated subalgebras of \(X_n^*\). Those statistics are automorphism-invariants, but they do not separate all algebra elements and do not imply that the automorphism group is trivial. The present argument instead uses the full inter-level incidence pattern of the dual poset and canonically reconstructs every point.

## Verification
`verify_rigidity.py` exhaustively checks the adjacent-level incidence characterization for widths up to six points, verifies the endpoint and unique-missing-neighbor descriptions through width 101, checks the iterated label reconstruction, and enumerates finite compatible level-permutation chains for manageable widths. It returns:

```text
VERIFY_OK 202219 exact assertions
```

The finite replay is a transcription and boundary check; the all-\(n\) theorem is proved by the symbolic order argument above.

## Relationship to prior work
The source explicitly defines the spaces \(X_n\), proves that they are Esakia spaces, establishes that \(X_n^*\) is infinite and \((n+1)\)-generated, and uses them to prove strict \(n\)-finiteness. The inspected article contains no occurrence of “automorphism” or “rigid,” and targeted searches did not locate an equivalent rigidity theorem for this family.

The closest owned results are the exact monogenic spectrum for \(X_2^*\) and its uniform extension to all \(n\ge1\). They concern one-generated subalgebra sizes rather than automorphism groups. Candidate-specific published-finding corpus searches likewise returned unrelated rigidity and automorphism results, but no result about these \(X_n\).

## Limitations
The originality risk is that the rigidity argument is short and may be known informally or appear in unindexed notes. The \(n=0\) endpoint may also be classical through the Rieger--Nishimura lattice. The claimed contribution is the uniform all-\(n\) rigidity theorem for the canonical strict-finiteness family and its immediate dual Heyting-algebra consequence.

## References
1. Tapani Hyttinen and Davide Emilio Quadrellaro, *Varieties of strictly n-generated Heyting algebras*, arXiv:2306.12250, first posted 21 June 2023.
2. Tapani Hyttinen, Miguel Martins, Tommaso Moraschini, and Davide E. Quadrellaro, *Strictly n-finite varieties of Heyting algebras*, Journal of Symbolic Logic, DOI: 10.1017/jsl.2024.48. Definition 4.1 gives \(X_n\); Section 2 recalls Esakia duality; Corollary 4.4 identifies \(X_n^*\) as infinite and \((n+1)\)-generated.
