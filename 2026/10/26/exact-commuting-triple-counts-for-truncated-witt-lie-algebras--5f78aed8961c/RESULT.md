# Exact commuting-triple counts for truncated Witt Lie algebras

## Finding

For an odd prime \(p\ge3\), an integer \(e\ge1\), and \(q=p^e\), consider the \(p\)-dimensional restricted Witt Lie algebra \(W=\operatorname{Der}_{\mathbb F_q}(\mathbb F_q[x]/(x^p))\). The number \(T_{p,q}\) of **ordered pairwise-commuting triples** in \(W\), including zero elements, is

\[
\boxed{T_{p,q}=(q+1)^2q^{3t-1}+(q^2-1)q^{2t+1}-(2q+1)q^{2t-1}},\qquad t=(p-1)/2.
\]

An auxiliary formula gives the number of commuting ordered pairs:

\[
\boxed{K_2(W)=q^{p+1}+t(q^2-1)q^{p-2}}.
\]

These formulas hold in every extension field of odd prime characteristic, including the boundary \(p=3\).

## Assumptions and scope

Write \(A=\mathbb F_q[x]/(x^p)\), \(\partial=d/dx\), and identify an element of \(W\) with \(f\partial\) for \(f\in A\). The bracket is \([f\partial,g\partial]=(fg'-gf')\partial\). The \(x\)-adic order \(v(f)\) is the smallest exponent with nonzero coefficient, and \(v(0)=p\). Put \(B_m=x^mA\partial\); only \(2\le m\le t+1\) enters the auxiliary count. All dimensions and ranks are over \(\mathbb F_q\), and all tuple coordinates are ordered.

## Proof

**1. Centralizer rank.** For \(f=a_vx^v+\text{higher terms}\), with \(a_v\ne0\), the adjoint map on the basis \(x^j\partial\), \(0\le j\le p-1\), has output with initial coefficient \(a_v(j-v)x^{v+j-1}\), whenever \(0\le j\le p-v\). For \(j\ne v\) these initial monomials are distinct. If \(2v\le p-1\), the exceptional column \(j=v\) has support only in degrees at least \(2v\) and is spanned by the later pivot columns \(j=v+1,\ldots,p-v\). If \(2v\ge p+1\), no exceptional column lies in the active range. The same leading-term calculation covers \(v=1\), while for \(v=0\), differentiation of \(g/f\) (valid because \(f\) is a unit) gives a one-dimensional centralizer. Consequently

\[
\dim C_W(f)=
\begin{cases}
p,&f=0,\\
1,&v(f)=0\text{ or }1,\\
v(f),&2\le v(f)\le t,\\
v(f)-1,&t+1\le v(f)\le p-1.
\end{cases}
\]

**2. The centralizers as Lie algebras.** If \(2\le v\le t\), then \(f\) commutes with every element of \(B_{p-v+1}\), since all resulting bracket monomials have degree at least \(p\). Moreover \(f\notin B_{p-v+1}\), so dimension comparison yields

\[C_W(f)=\mathbb F_q f\oplus B_{p-v+1}.\]

Since \(2(p-v+1)-1\ge p\), the second summand is abelian; hence \(C_W(f)\) is abelian. If \(t+1\le v\le p-1\), the same containment and dimension comparison give \(C_W(f)=B_{p-v+1}\). For \(v=0,1\), the centralizer is the abelian line \(\mathbb F_q f\).

**3. Pair counts in the high-order subalgebras.** Fix \(2\le m\le t+1\). The subalgebra \(B_m\) has dimension \(p-m\). Its central elements include exactly the elements divisible by \(x^{p-m+1}\); this subspace has \(q^{m-1}\) elements. For \(f\in B_m\) with order \(m\le v\le p-m\), the leading-column argument restricted to \(x^j\partial\) with \(m\le j\le p-1\) gives

\[
\operatorname{rank}(\operatorname{ad}_f|_{B_m})=p-v-m+1-\mathbf1_{v\le t}.
\]

For each \(v\) the number of elements of order \(v\) is \((q-1)q^{p-v-1}\). The central region contributes \(q^{p-1}\) commuting pairs. Each of the \(t+1-m\) orders in \([m,t]\) contributes \((q-1)q^{p-1}\), and each of the same number in \([t+1,p-m]\) contributes \((q-1)q^{p-2}\). Therefore

\[
\boxed{K_2(B_m)=q^{p-1}+(t+1-m)(q^2-1)q^{p-2}.}
\]

This includes the abelian endpoint \(m=t+1\).

**4. Pairs in the whole Witt algebra.** The zero first element contributes \(q^p\). Exactly \((q^2-1)q^{p-2}\) nonzero elements have orders zero or one, each with a \(q\)-element centralizer. Each order \(v\) with \(2\le v\le t\) contributes \((q-1)q^{p-1}\) pairs; each order \(t+1\le v\le p-1\) contributes \((q-1)q^{p-2}\) pairs. There are \(t-1\) and \(t\) such orders respectively. Summation yields \(K_2(W)=q^{p+1}+t(q^2-1)q^{p-2}\).

**5. Commuting triples.** Fix the first element \(f\). The other two must be a commuting ordered pair inside its Lie centralizer. Thus zero contributes \(K_2(W)\); orders zero and one together contribute \((q^2-1)q^p\); orders \(2\le v\le t\) contribute \((q-1)q^{p+v-1}\) each; and for \(t+1\le v\le p-1\), substitution \(m=p-v+1\) gives \((q-1)q^{m-2}K_2(B_m)\). Hence the independently checkable finite sum is

\[
T_{p,q}=K_2(W)+(q^2-1)q^p
 +(q-1)\sum_{v=2}^{t}q^{p+v-1}
 +(q-1)\sum_{m=2}^{t+1}q^{m-2}
 \left[q^{p-1}+(t+1-m)(q^2-1)q^{p-2}\right].
\]

The first sum is empty at \(p=3\). Applying the geometric sum and its derivative and collecting powers gives the displayed closed form. Each step is equality over integers; no asymptotic or probabilistic approximation is involved.

## Verification

The included `verify.py` computes literal brackets \([f\partial,g\partial]\), modular adjoint-matrix ranks, and commuting-pair counts independently of the formulas. It exhausts the entire Witt algebra in \(\mathbb F_3\) and \(\mathbb F_9\), as well as \(\mathbb F_5\), checks the full triple count by direct enumeration for \(p=q=3\), and checks the nonabelian subalgebra-pair contribution directly for \(p=q=5\). It tests deterministic rank samples in \(\mathbb F_7\) and \(\mathbb F_{25}\). Execution gives `VERIFY_OK_WITT_COMMUTING_TRIPLES`. Finite tests are corroboration, not a substitute for the proof.

## Relationship to prior work

The truncated Witt algebra and restricted structure are classical (Evans--Fuchs). The orbit and nilpotent-locus literature studies different invariants. Yao--Chang describe commuting-pair varieties, and Yao--Zhang analyze components and dimensions of varieties of commuting tuples over algebraically closed fields. These geometric results motivate an exact rational-point-count question; an irreducible-component list and its dimensions do not by themselves specify the exact number of finite-field rational points. No direct formula of the present finite-field counting form was identified in the inspected accessible texts and bibliographic searches. The 2021 tuple-variety article was accessible here at abstract level only, so implicit coverage is a genuine unresolved priority risk.

## Limitations

The formula concerns only three commuting elements of the truncated one-variable Witt algebra in odd prime characteristic. It does not classify the commuting-triple scheme, its singularities, nilpotent restrictions, general tuple lengths, or Lie algebra isomorphism classes. Full-text priority comparison with all geometrically related articles has not been completed. Verification is computational only for specified fields; independent review has not been performed.

## References

- Evans and Fuchs, *On the Restricted Lie Algebra Structure for the Witt Lie Algebra in Finite Characteristic*, arXiv:math/0111271 (first publicly posted 2001-11-27), https://arxiv.org/abs/math/0111271.
- Yao and Chang, *Borel subalgebras of the Witt algebra W1*, arXiv:1212.4349 (2012), https://arxiv.org/abs/1212.4349.
- Yao and Chang, *Commuting variety of Witt algebra*, Frontiers of Mathematics in China 13 (2018), https://doi.org/10.1007/s11464-018-0725-9.
- Yao and Zhang, *Commuting variety of r-tuples over the Witt algebra*, Journal of East China Normal University (2021), https://doi.org/10.3969/j.issn.1000-5641.2021.03.001.
- Li, *On nilpotent commuting varieties of r-tuples in the Witt algebra*, Journal of Pure and Applied Algebra (2015), https://doi.org/10.1016/j.jpaa.2015.02.005.
