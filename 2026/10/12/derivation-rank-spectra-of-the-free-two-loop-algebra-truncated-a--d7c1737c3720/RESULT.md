# Derivation-rank spectra of the free two-loop algebra truncated at length three

## Finding

Let \(q\) be any prime power and put
\[
\mathcal A_q=\mathbb F_q\langle x,y\rangle/(x,y)^3.
\]
This is the **noncommutative**, seven-dimensional unital associative algebra with ordered basis \(1,x,y,x^2,xy,yx,y^2\); all words of length at least three vanish, but \(xy\) and \(yx\) remain distinct. Every derivation is an \(\mathbb F_q\)-linear endomorphism of this seven-dimensional space. Define its complete operator-rank enumerator by
\[
H_q(T)=\sum_{D\in\operatorname{Der}_{\mathbb F_q}(\mathcal A_q)}T^{\operatorname{rank}_{\mathbb F_q}(D)}.
\]
Write
\[
G=(q^2-1)(q^2-q),\qquad N_1=\frac{(q^4-1)(q^2-1)}{q-1},\qquad N_2=(q^4-1)(q^4-q),
\]
and \(B_q(T)=1+N_1T+N_2T^2\). Then, **if \(q\) is odd**,
\[
\begin{aligned}
H_q(T)={}&B_q(T)+(q^2-1)q^6\bigl(T^3+(q^2-1)T^4\bigr)\\
&+q(q^2-1)q^7\bigl(T^4+(q-1)T^5\bigr)\\
&+q^2(q-1)q^8T^4+\bigl(G-q^2(q-1)\bigr)q^8T^6.
\end{aligned}
\]
If **\(q\) is even**,
\[
\begin{aligned}
H_q(T)={}&B_q(T)+(q-1)q^8T^2\\
&+(q+1)(q^2-1)q^6\bigl(T^3+(q^2-1)T^4\bigr)\\
&+\bigl(G-(q-1)\bigr)q^8T^4.
\end{aligned}
\]
In every characteristic \(H_q(1)=q^{12}\). Thus every rank from zero to six occurs in odd characteristic, whereas exactly ranks zero through four occur in characteristic two; no derivation of rank five or six exists in characteristic two. In particular,
\[
H_2(T)=1+45T+466T^2+576T^3+3008T^4,
\]
\[
H_3(T)=1+320T+6240T^2+5832T^3+217242T^4+104976T^5+196830T^6.
\]

## Assumptions and scope

The ring is the **associative** quotient of the unital free algebra in two noncommuting generators by the ideal spanned by words of length at least three. Derivations are all \(\mathbb F_q\)-linear Leibniz derivations, including non-inner ones; rank refers to the induced linear endomorphism on the *whole* algebra. The formula is valid for every prime power, including nonprime fields, with no assumption on the existence of a scalar splitting of a characteristic polynomial.

## Proof

**1. All derivations have twelve free parameters.** For any derivation \(D\), the Leibniz rule gives \(D(1)=0\). Write the scalar coefficients of \(D(x),D(y)\) as \(\alpha,\beta\). Applying \(D\) to the relation \(xyx=0\) and retaining degree two gives
\[
\alpha(yx+xy)+\beta x^2=0.
\]
The three displayed words are linearly independent in the quotient in every characteristic, forcing \(\alpha=\beta=0\). Conversely, any choice of images of \(x,y\) in the six-dimensional augmentation ideal extends uniquely to a derivation: replacing a letter in a word of length three by any positive-degree word leaves a word of length at least three, hence zero. Thus \(\dim\operatorname{Der}(\mathcal A_q)=12\).

Let \(V=\operatorname{span}\{x,y\}\) and \(W=\operatorname{span}\{x^2,xy,yx,y^2\}=V\otimes V\). The restriction to the augmentation ideal is block triangular:
\[
D\big|_{V\oplus W}=\begin{pmatrix}A&0\\ B&L_A\end{pmatrix},
\quad A\in M_2(\mathbb F_q),\quad B\in M_{4\times2}(\mathbb F_q),
\quad L_A=A\otimes I_2+I_2\otimes A.
\]
Both \(A\) and \(B\) vary independently, and \(D(1)=0\) does not contribute to rank.

**2. The rank of the tensor-square block.** Put \(a=\operatorname{rank}A\), \(\ell=\operatorname{rank}L_A\), and \(G=|\mathrm{GL}_2(\mathbb F_q)|\). The complete disjoint classification of \(A\) is:

| Characteristic | Kind of \(A\) | Count | \(a\) | \(\ell\) |
|---|---|---:|---:|---:|
| odd | zero | \(1\) | 0 | 0 |
| odd | nonzero nilpotent | \(q^2-1\) | 1 | 2 |
| odd | rank one, nonnilpotent | \(q(q^2-1)\) | 1 | 3 |
| odd | invertible, trace zero | \(q^2(q-1)\) | 2 | 2 |
| odd | invertible, nonzero trace | \(G-q^2(q-1)\) | 2 | 4 |
| even | zero | \(1\) | 0 | 0 |
| even | nonzero scalar | \(q-1\) | 2 | 0 |
| even | rank one | \((q+1)(q^2-1)\) | 1 | 2 |
| even | invertible nonscalar | \(G-(q-1)\) | 2 | 2 |

To verify the block ranks, extend scalars to a splitting field (this preserves rank). For a diagonal matrix with eigenvalues \(\lambda,\mu\), the eigenvalues of \(L_A\) are \(2\lambda,\lambda+\mu,\lambda+\mu,2\mu\). A nonsemisimple Jordan block \(A=\lambda I+N\), \(N^2=0\ne N\), gives \(L_A=2\lambda I+(N\otimes I+I\otimes N)\), where the nilpotent summand has rank exactly two. These observations prove all listed \(\ell\), in particular rank two for every nonscalar \(A\) in characteristic two and rank zero for every scalar \(A\) in that characteristic. Standard rank-one matrix enumeration gives \((q+1)(q^2-1)\) matrices, of which \(q^2-1\) are nonzero nilpotent; in odd characteristic the trace-zero subspace has \(q^3\) matrices, precisely \(q^2\) of them singular, giving \(q^2(q-1)\) invertible trace-zero matrices.

**3. Counting the arbitrary lower-left block.** Let \(t=4-\ell\) and \(k=2-a\). Reducing the bottom block modulo \(\operatorname{im}L_A\) gives
\[
\operatorname{rank}D=\ell+a+\operatorname{rank}\left(\ker A\xrightarrow{\,B\,}W/\operatorname{im}L_A\right).
\]
For prescribed rank \(j\) of the last map, the number of choices of \(B\) is exactly
\[
q^{2\ell+ta}{t\brack j}_q{k\brack j}_q|\mathrm{GL}_j(\mathbb F_q)|.
\]
Indeed, the projection of each of the two columns of \(B\) to \(W/\operatorname{im}L_A\) has \(q^{\ell}\) lifts; on a complement to \(\ker A\) its values are arbitrary (\(q^{ta}\) choices); and its restriction to the kernel is a rank-\(j\) map from a \(k\)-space to a \(t\)-space. The latter has exactly the displayed Gaussian-binomial count. For \(A=0\), this is the standard rank distribution for \(4\times2\) matrices, namely \(1,N_1,N_2\). Substituting every line of the classification table proves the two displayed formulas. Summing over \(A,B\) yields \(q^4q^8=q^{12}\) by construction; every asserted nonzero coefficient is positive for its characteristic range.

## Verification

The standalone script `verify.py`, using only the Python standard library, constructs the derivation operator directly from its generator images; it does **not** construct it from the symbolic stratum formula. Executing `python3 verify.py` checks that the full \(49\)-unknown Leibniz linear system has rank \(37\) over fields of orders two and three, hence a twelve-dimensional solution space. It exhaustively computes all \(2^{12}=4096\) and \(3^{12}=531441\) derivation ranks and compares their complete histograms with the formulas; it also checks selected operators over the nonprime field of order four and exact coefficient normalization at additional prime field orders. It terminates with `VERIFY_OK_FREE_TRUNC_DERIV`. Finite checks support but do not replace the general proof.

## Relationship to prior work

Strametz's 2001 monomial-algebra treatment describes first Hochschild cohomology and derivations in terms of parallel paths and a graded Lie structure, including truncated quiver examples. Xu–Han–Jiang (2005) calculate Hochschild cohomology of truncated quiver algebras in arbitrary characteristic. Sánchez-Flores (2010) studies outer derivations and describes the radical-square-zero multiple-loop case. These works establish important structural context, but their inspected results do not give the operator-rank multiplicities of **all derivations** of this particular two-loop length-three quotient or the characteristic-two rank ceiling. Cohomology-space dimensions and brackets do not by themselves specify the rank distribution of the endomorphisms representing derivations. A commutative quotient replaces the tensor-square summand \(V\otimes V\) by \(\operatorname{Sym}^2 V\), so its derivation-rank enumerator cannot be substituted for the one above.

## Limitations

The theorem treats precisely two noncommuting generators and word-length truncation three, not arbitrary quivers, longer truncations, derivation conjugacy, or outer-derivation rank modulo inner derivations. The proof is algebraic, not dependent on exhaustive enumerations. The bibliographic comparison was targeted; an earlier equivalent rank-count formula under unfamiliar terminology remains possible and has not received independent verification.

## References

1. C. Strametz, *The Lie algebra structure on the first Hochschild cohomology group of a monomial algebra*, arXiv:math/0111060v1 (first public 2001-11-06); full text https://arxiv.org/html/math/0111060v2, especially Sections 2 and 4.
2. Y. Xu, Y. Han, W. Jiang, *Hochschild cohomology of truncated quiver algebras*, arXiv:math/0509202v1 (2005-09-09), https://arxiv.org/html/math/0509202v1, particularly Section 1.
3. S. Sánchez-Flores, *On the semisimplicity of the outer derivations of monomial algebras*, arXiv:1004.2820v1 (2010-04-16), https://arxiv.org/html/1004.2820v1, Sections 1–2.
