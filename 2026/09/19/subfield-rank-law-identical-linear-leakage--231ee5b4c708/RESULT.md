# Subfield-rank law for identical leakage under linear computations

## Statement

Let \(B=\mathbb F_q\subset F=\mathbb F_{q^m}\), and let
\(G\in F^{K\times N}\) have row rank \(K\). Write its columns as
\(g_1,\ldots,g_N\in F^K\), and define the **column subfield rank**

\[
\rho_B(G):=\dim_B\operatorname{span}_B\{g_1,\ldots,g_N\}.
\]

Then

\[
K\le \rho_B(G)\le \min\{N,Km\}.
\]

The quantity is unchanged by left multiplication of \(G\) by an element of
\(\mathrm{GL}_K(F)\), so it is an invariant of the computation code together
with its output coordinates.

Consider one share position of \(K\) independent \(F\)-valued wires,
represented by \(x\in F^K\). The \(i\)-th computed wire contains
\(g_i^T x\). Suppose the *same* nonzero \(B\)-linear one-symbol leakage map
\(\lambda:F\to B\) is applied to every computed wire. Then the joint leakage
map

\[
L_{G,\lambda}:F^K\to B^N,
\qquad
x\mapsto \bigl(\lambda(g_1^Tx),\ldots,\lambda(g_N^Tx)\bigr)
\]

has exact \(B\)-rank

\[
\boxed{\operatorname{rank}_B L_{G,\lambda}=\rho_B(G).}
\]

Moreover, if \(I\subseteq[N]\) indexes \(\rho_B(G)\) columns forming a
\(B\)-basis of the column span, then the leakage on those coordinates determines
all \(N\) leaked symbols by a fixed \(B\)-linear map. Thus
\(\rho_B(G)\), rather than \(N\), is the exact number of independent reused
one-symbol leakage projections created locally by the computation.

Two extremal consequences are particularly useful.

1. **No-amplification regime.** \(\rho_B(G)=K\) if and only if the
   computation code descends to \(B\): after an invertible change of input basis,
   it has a generator matrix with entries in \(B\). In this case identical
   \(B\)-linear leakage on all \(N\) computed wires contains exactly the same
   information as identical leakage on \(K\) independent wires.

2. **Full-disclosure regime.** If \(\rho_B(G)=Km\), then for every nonzero
   \(B\)-linear \(\lambda\), the reused leakage values at a single share
   position determine the entire vector \(x\in F^K\). In particular, when the
   same nonzero leakage map is used at every share position, all underlying
   shares are recovered before any coding-theoretic reconstruction is needed.

## Exact consequence for Massey/LERS leakage

Let \(C_0\subseteq F^{n+1}\) be a base linear code used for Massey secret
sharing. Take arbitrary independent codewords
\(c^{(1)},\ldots,c^{(K)}\in C_0\), and define the \(N\) computation streams by

\[
c_i=\sum_{a=1}^K G_{a,i}c^{(a)} \qquad (i\in[N]).
\]

At share position \(j\), suppose every stream is subjected to the same
\(B\)-linear map \(\lambda_j:F\to B\), as in the identical-leakage model of
Aoutouf--Augot.

If \(\rho_B(G)=K\), then there is a \(B\)-linear reconstruction of all \(K\)
input secrets from the computed-stream leakage **if and only if** the base code
\(C_0\) itself admits the one-symbol LERS using the maps
\(\lambda_1,\ldots,\lambda_n\). Thus no parameter improvement over the base
LERS can be obtained from *any* computation code that descends to \(B\).

This proves, in particular, that the no-improvement observation for simple
addition extends to every array-summation network and, more generally, to every
linear computation whose coefficients are defined over the leakage subfield
(after an invertible input change of basis).

## Proof

Every \(B\)-linear functional \(\lambda:F\to B\) has a unique representation

\[
\lambda(z)=\operatorname{Tr}_{F/B}(\beta z)
\]

for some \(\beta\in F\), because the finite-field trace pairing is
nondegenerate. The assumption that \(\lambda\ne0\) is equivalent to
\(\beta\ne0\).

Consider the nondegenerate \(B\)-bilinear pairing on \(F^K\),

\[
\langle a,x\rangle=\operatorname{Tr}_{F/B}(a^Tx).
\]

The \(i\)-th component of \(L_{G,\lambda}\) is the functional

\[
x\longmapsto \operatorname{Tr}_{F/B}(\beta g_i^Tx).
\]

Under the trace-pairing isomorphism between \(F^K\) and its \(B\)-linear dual,
this functional corresponds to the coefficient vector \(\beta g_i\). Since
multiplication by \(\beta\ne0\) is a \(B\)-linear automorphism,

\[
\dim_B\operatorname{span}_B\{\beta g_i:i\in[N]\}
=
\dim_B\operatorname{span}_B\{g_i:i\in[N]\}
=\rho_B(G),
\]

which proves the rank formula.

For the compression statement, choose basis columns
\(g_{i_1},\ldots,g_{i_d}\), where \(d=\rho_B(G)\). Each column has a unique
expression

\[
g_i=\sum_{t=1}^d a_{t,i}g_{i_t},\qquad a_{t,i}\in B.
\]

Hence, by \(B\)-linearity of \(\lambda\),

\[
\lambda(g_i^Tx)=\sum_{t=1}^d a_{t,i}\lambda(g_{i_t}^Tx).
\]

Thus the selected \(d\) leaked coordinates generate the complete transcript.
The rank formula shows that none of these \(d\) coordinates is redundant as a
functional of \(x\).

For the descent criterion, suppose first that \(\rho_B(G)=K\). Pick a
\(B\)-basis \(u_1,\ldots,u_K\) of the column span. These vectors must also be
\(F\)-linearly independent: otherwise their \(F\)-span would have dimension
less than \(K\), while it contains every column of \(G\), contradicting
\(\operatorname{rank}_F G=K\). Let \(U=[u_1\ \cdots\ u_K]\in\mathrm{GL}_K(F)\).
Every column of \(U^{-1}G\) lies in \(B^K\), so \(U^{-1}G\) is a generator over
\(B\). Conversely, a full-row-rank generator with entries in \(B\) has
\(B\)-column rank exactly \(K\).

When \(d=K\), the selected basis columns form an invertible \(K\times K\)
matrix over \(F\). Therefore the selected \(K\) computation streams are an
invertible \(F\)-linear change of variables of the \(K\) independent base-code
streams, and they range freely over \(C_0^K\). All remaining leakage values are
\(B\)-linear combinations of their leakage values. If a \(B\)-linear decoder
recovers the \(K\) secrets from the full computed transcript, restrict it to
instances where all but one selected stream are zero. This gives a one-symbol
LERS for \(C_0\) with the same maps \(\lambda_j\). The converse follows by
running the base LERS independently on the selected streams and inverting the
\(F\)-linear change of variables.

Finally, if \(d=Km\), the local map \(L_{G,\lambda}\) has rank equal to the
\(B\)-dimension of its domain \(F^K\), hence is injective. This proves full
local disclosure.

## Structural examples

### Simple addition and array summation

All coefficients in the usual addition and partial-sum computation matrices lie
in the prime subfield, hence in \(B\). Their computation generators have
\(\rho_B(G)=K\). Identical linear leakage therefore gives no more independent
subsymbols than the \(K\) original streams. This turns the tentative extension
to array summation noted by Aoutouf--Augot into a general theorem for all
subfield-rational linear computation networks.

### A three-wire relation

For

\[
w=\mu_u u+\mu_v v,
\qquad
G=\begin{bmatrix}1&0&\mu_u\\0&1&\mu_v\end{bmatrix},
\]

one has

\[
\boxed{\rho_B(G)=2\ \Longleftrightarrow\ (\mu_u,\mu_v)\in B^2,}
\]

and otherwise \(\rho_B(G)=3\). Thus an extension-field coefficient outside
\(B\) is necessary and sufficient for this relation to create even one extra
independent reused-leakage projection locally. In particular, over base fields
larger than \(\mathbb F_2\), merely requiring
\(\mu_u,\mu_v\notin\{0,1\}\) is not enough: coefficients lying in
\(B\setminus\{0,1\}\) remain in the no-amplification regime. This is a local
information statement and does not by itself guarantee that a global LERS
exists when \(\rho_B(G)>K\).

### LFSR and rank saturation

For the one-input LFSR computation

\[
G=(1,\alpha,\alpha^2,\ldots,\alpha^{N-1}),
\]

\[
\rho_B(G)=\dim_B\operatorname{span}_B\{1,\alpha,\ldots,\alpha^{N-1}\}.
\]

If \(N\ge m\) and these coefficients span \(F\) over \(B\), then
\(\rho_B(G)=m\), so one repeated trace leakage per iteration determines the
entire share. This recovers the LFSR phenomenon in the motivating paper as the
rank-saturated \(K=1\) endpoint of the general law.

## Random systematic computation layers

The rank law also gives a sharp threshold for a natural random model. Take

\[
G=[I_K\mid R],
\]

where the \(L=N-K\) columns of \(R\in F^{K\times L}\) are independent and
uniform in \(F^K\). Let

\[
D=K(m-1)=\dim_B(F^K/B^K).
\]

Projection modulo \(B^K\) turns the random columns into independent uniform
vectors in a \(D\)-dimensional \(B\)-space, and therefore

\[
\rho_B(G)=K+\operatorname{rank}_B(\overline R).
\]

In particular, for \(L\ge D\),

\[
\boxed{
\Pr[\rho_B(G)=Km]
=
\prod_{i=0}^{D-1}\left(1-q^{i-L}\right).
}
\]

For \(L=D+s\), a union bound gives

\[
\Pr[\rho_B(G)=Km]
\ge
1-\frac{q^{-s}(1-q^{-D})}{q-1}.
\]

Thus once a random systematic linear computation exposes roughly \(Km\)
streams, reused one-symbol leakage is already in the complete local-disclosure
regime with substantial probability, and with probability approaching one after
only a constant number of additional random outputs. Conversely,

\[
\Pr[\rho_B(G)=K]=q^{-DL},
\]

so exact no-amplification is exceptional for random extension-field
coefficients when \(m>1\).

## Relation to prior work and originality boundary

Aoutouf and Augot introduced the product-code framework for LERS-derived leakage
under linear computations and proved that simple addition gives no improvement
when leakage functions are identical. They wrote that the same argument
"seems to extend directly" to array summation, while simulations suggested that
more general extension-field relations and LFSRs can still benefit from
identical leakage. Their Section 5 does not give a general algebraic criterion
for when identical leakage can create additional independent projections.

The column-span quantity used here is a standard rank-metric/subfield-rank
notion; no novelty is claimed for rank weight, rank support, trace duality, or
field-of-definition criteria themselves. The new claim is the exact identity
between that subfield rank and the number of independent reused leakage
functionals, together with the resulting no-amplification theorem for all
subfield-rational computations, the full-disclosure endpoint, and the random
systematic threshold.

To the best of our knowledge, targeted searches for identical/reused leakage
under linear computations, subfield/rank-weight formulations of the computation
matrix, and equivalent trace-leakage statements did not locate this criterion or
its corollaries. Because the motivating preprint is very recent and the proof is
short linear algebra once the invariant is identified, near-simultaneous and
folklore priority risk remains material.

## Verification

`artifacts/verify_subfield_rank.py` independently checks finite-field instances
in characteristic two. It verifies the equality between column subfield rank
and trace-functional rank for random matrices over \(\mathbb F_{2^m}\),
\(m=2,3,4\); checks exact transcript reduction for a base-field computation
matrix; checks injectivity in rank-saturated one-input examples; and exhaustively
checks the full-rank probability count for small random binary quotient matrices.
The recorded output is in `artifacts/verification.txt`.

The finite checks are sanity tests; the theorem is proved algebraically above.

## Limitations

The theorem concerns identical **one-symbol \(B\)-linear** leakage maps across
computed streams. It does not classify nonlinear leakage, independently chosen
leakage functions, refreshed shares, or multiplication/Schur-product
computations. The intermediate regime \(K<\rho_B(G)<Km\) quantifies local
leakage dimension but does not by itself decide whether the base/product code
admits a global LERS. The result therefore complements rather than replaces the
subfield-subcode rank criterion of Aoutouf--Augot.

## References

1. N. Aoutouf and D. Augot, *On the Leakage of Massey Secret Sharing Schemes under Linear Computations*, arXiv:2609.19929, 17 Sep 2026. https://arxiv.org/abs/2609.19929
2. N. Aoutouf and D. Augot, *A Subfield Subcode Construction of a Linear Exact Repair Scheme*, WCC 2026. https://wcc2026.inria.fr/assets/final_versions/WCC2026_paper_33.pdf
3. F. Benhamouda, A. Degwekar, Y. Ishai, and T. Rabin, *On the Local Leakage Resilience of Linear Secret Sharing Schemes*, CRYPTO 2018 / J. Cryptology 2021. https://eprint.iacr.org/2019/653
4. V. Guruswami and M. Wootters, *Repairing Reed-Solomon Codes*, STOC 2016. https://doi.org/10.1145/2897518.2897525
