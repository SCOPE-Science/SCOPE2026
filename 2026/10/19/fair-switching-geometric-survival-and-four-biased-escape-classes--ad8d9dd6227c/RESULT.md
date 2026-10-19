# Fair-switching geometric survival and four biased escape classes for binary Markov holes

## Finding

For the doubling map \(T(x)=2x\bmod 1\) on \([0,1)\), let \(H_{ij}\) be the half-open binary cylinder whose first two binary digits are \(i,j\in\{0,1\}\). Select two **distinct** cylinders \(H_a,H_b\). At every iterate, independently of the past and of the starting point, choose hole \(H_a\) with probability \(p\) and hole \(H_b\) with probability \(1-p\). Remove a point if its current iterate belongs to the selected hole. The starting point is Lebesgue-uniform, and \(S_n\) denotes the joint (annealed) probability of surviving observations \(0,\ldots,n-1\), with \(S_0=1\).

**Fair-switching universality.** For **every** one of the six unordered pairs of distinct binary length-two cylinders, independent fair selection yields the exact law
\[
S_n=\left(\frac34\right)^n\qquad(n\ge0).
\]
This law holds even for pairs whose two-cylinder union does not cover all binary states evenly; it therefore does not follow from a spatially constant one-step hazard.

**Sharp bias classification.** Set \(\frac12<p<1\), so \(a\) is the more probable hole. Every one of the twelve ordered choices of distinct cylinders belongs to one of the following four classes; \(\ell\) means a loop word \(00\) or \(11\), while \(c\) means a cross word \(01\) or \(10\). The classes are respectively \(A=(\ell,c)\) (four choices), \(B=(\ell,\ell)\) (two choices), \(C=(c,c)\) (two choices), and \(D=(c,\ell)\) (four choices). For each class \(j\), the entire survival sequence has generating function
\[
\sum_{n\ge0}S_n^{(j)}z^n=\frac{1+(3/4-t_j)z}{1-t_jz+d_jz^2},
\qquad S_0^{(j)}=1,\quad S_1^{(j)}=\frac34,
\quad S_{n+2}^{(j)}=t_j S_{n+1}^{(j)}-d_j S_n^{(j)}.
\]
The exact coefficients are:

| Class \(j\) | \(t_j\) | \(d_j\) | \(S_2^{(j)}\) |
|---|---|---|---|
| \(A\) | \(1-p/2\) | \((1-2p)/4\) | \((p+4)/8\) |
| \(B\) | \(1/2\) | \(-(1-p+p^2)/4\) | \((2p^2-2p+5)/8\) |
| \(C\) | \(1\) | \((1-p+p^2)/4\) | \((2+p-p^2)/4\) |
| \(D\) | \((1+p)/2\) | \((2p-1)/4\) | \((5-p)/8\) |

In particular,
\[
S_2^{(A)}>S_2^{(B)}>S_2^{(C)}>S_2^{(D)}
\qquad\left(\frac12<p<1\right).
\]
Let \(\lambda_j\) be the Perron root, i.e., the larger root of \(\lambda^2-t_j\lambda+d_j=0\). The four **asymptotic survival radii** are also strictly ordered for every bias:
\[
\lambda_A>\lambda_B>\lambda_C>\lambda_D,
\quad \lim_{n\to\infty}S_n^{(j)1/n}=\lambda_j,
\quad \gamma_j=-\log\lambda_j.
\]
Consequently the corresponding escape rates satisfy \(\gamma_A<\gamma_B<\gamma_C<\gamma_D\). Swapping the two hole names covers \(0<p<1/2\). The fair value \(p=1/2\) is the only mixing parameter in \(0<p<1\) for which **all twelve** ordered pairs have the stated exact geometric law \(S_n=(3/4)^n\).

## Assumptions and scope

The holes are precisely the four half-open dyadic cylinders \(H_{00}=[0,1/4)\), \(H_{01}=[1/4,1/2)\), \(H_{10}=[1/2,3/4)\), and \(H_{11}=[3/4,1)\). Ambiguous binary expansions at dyadic rationals form a Lebesgue-null set and do not affect the result. Holes are selected anew at **each** step, independently, and the displayed probabilities average jointly over the initial point and the hole sequence. The theorem does not describe survival conditional on a fixed realization of the random holes (quenched survival), nor does it address holes of other lengths or general expanding maps. The two selected hole words must be distinct. Throughout \(0<p<1\) every allowed matrix entry is positive.

## Proof

Let \(X_k\in\{0,1\}\) be the \(k\)-th binary digit of a Lebesgue-random point. These digits are independent and fair. At step \(k\), the orbit belongs to \(H_{ij}\) precisely when \((X_{k+1},X_{k+2})=(i,j)\). The probability of avoiding the randomly chosen hole, conditional on those two digits, is
\[
w_{ij}=1-p\mathbf 1_{\{ij=a\}}-(1-p)\mathbf 1_{\{ij=b\}}.
\]
Independence of the hole choices conditional on the digit sequence yields an exact transfer matrix, with entries \(M_{ij}=w_{ij}/2\). If \(\mathbf 1=(1,1)^\mathsf T\) and \(u=(1/2,1/2)\), summing all \(n+1\)-digit paths gives
\[
S_n=uM^n\mathbf 1\quad(n\ge0).
\]
This identity is exact, not an asymptotic transfer-operator approximation. Every \(M\) has sum of entries equal to \(3/2\), hence \(S_1=3/4\).

For \(p=1/2\), examine the six unordered pairs of distinct edges in the directed two-vertex graph. If the two removed edges are both loops or both cross edges, each row sum of \(M\) is exactly \(3/4\), so \(M\mathbf 1=(3/4)\mathbf 1\). Otherwise the pair contains one loop and one cross edge. The corresponding matrix is rank one and obeys the exact algebraic identity \(M^2=(3/4)M\) (regardless of the orientation of the chosen cross edge). In either case, \(S_0=1\), \(S_1=3/4\), and induction gives \(S_n=(3/4)^n\) for all integers \(n\ge0\).

For \(p>1/2\), the location of the high-weight forbidden edge (loop or cross) and of the second edge partitions the twelve assignments into four classes. In each class direct substitution into \(M\), using only a simultaneous permutation of vertex labels when needed, yields exactly the \(t_j=\operatorname{tr}M\) and \(d_j=\det M\) tabulated above. The characteristic identity \(M^2-t_jM+d_jI=0\), multiplied on the left by \(uM^n\) and on the right by \(\mathbf 1\), establishes the claimed recurrence for all \(n\ge0\); summation gives the rational generating functions. The displayed second-survival formulas follow by \(S_2=(3/4)t_j-d_j\). Their consecutive positive differences are
\[
S_2^{(A)}-S_2^{(B)}=\frac{(2p-1)(1-p)}8,\quad
S_2^{(B)}-S_2^{(C)}=\frac{(2p-1)^2}8,\quad
S_2^{(C)}-S_2^{(D)}=\frac{(2p-1)(1-p)}8.
\]
[In the displayed differences, the algebraic identities can equivalently be checked by substituting the table; they are used only for the sign argument.]

The matrices have strictly positive entries when \(0<p<1\), so Perron--Frobenius theory yields a simple positive dominant root \(\lambda_j\) and a positive leading coefficient in \(uM^n\mathbf 1\). Hence the claimed root limit holds. To prove **strict** ordering for the whole bias range rather than extrapolating a few sample parameters, let \(\delta=p-1/2\in(0,1/2)\) and let \(P_j(X)=X^2-t_jX+d_j\). The exact consecutive polynomial resultants are
\[
\begin{split}
\operatorname{Res}(P_A,P_B)&=-\delta(2\delta-1)^2/32,\\
\operatorname{Res}(P_B,P_C)&=\delta^2(4\delta^2+3)/16,\\
\operatorname{Res}(P_C,P_D)&=\delta(2\delta-1)^3/64.
\end{split}
\]
None vanishes on the open interval. Therefore adjacent Perron roots, continuous in \(p\), cannot cross anywhere in that interval. At \(p=3/4\) the four roots are respectively
\[
\frac{5+\sqrt{57}}{16},\quad \frac{2+\sqrt{17}}8,\quad
\frac{4+\sqrt3}8,\quad \frac{7+\sqrt{17}}{16},
\]
which are strictly decreasing. This proves the four-class rate ordering for every \(1/2<p<1\). Finally, for \(p>1/2\) the tabulated second-step survivals are not all \(9/16\). Thus the exact all-pairs geometric law is impossible off \(p=1/2\); symmetry handles \(p<1/2\).

## Verification

The standalone `verify.py` performs exact symbolic checks of all twelve ordered-pair matrices, including their characteristic polynomials and survival generating functions; it verifies the three parameter-dependent resultants and the general algebraic identities used at fair mixing. It separately enumerates all digit paths through eight observations for several rational choices of \(p\), and confirms the ordering at \(p=3/4\). Running `python verify.py` with Python 3 and SymPy returns `VERIFY_OK`. The infinite-time conclusions are proved by the matrix argument and Perron--Frobenius theory, **not** by the finite enumeration.

## Relationship to prior work

Bahsoun--Vaienti (2012, arXiv:1206.3654) develop escape-rate theory for randomly perturbed maps and shrinking/random holes; their asymptotic perturbative estimates do not give this exact finite-horizon two-cylinder classification. Bahsoun--Schmeling--Vaienti (2014, arXiv:1405.0361) establish general weighted transfer-operator methods for random holes and treat explicit examples with a one-digit hole or nested ternary holes. These methods motivate the present finite-state representation, but the checked examples and propositions do not supply the four-class binary pair classification or the strict ordering as a stated result. Georgiou--Dettmann--Altmann (2012, arXiv:1207.7000) examine escape in fully chaotic maps, including uniformly resampled holes over all four length-two positions; uniform resampling from all four positions has a pointwise constant hazard. Here resampling uses only **two** of the four positions, generally has a nonconstant spatial hazard, yet still gives exact geometric survival when the two are equally likely. This distinguishes the present claim from the earlier all-four-hole observation. Comparisons with records on fixed or deterministically alternating holes address different selection protocols.

## Limitations

No quenched (fixed random environment) law, central limit theorem, finer finite-time ordering beyond the displayed \(n=2\) result, or generalization to longer cylinders is established. The novelty comparison is statement-level and not a proof that no equivalent formula exists in the broader pattern-matching or automata literature. General random-hole transfer theory is prior art; the claim is the **complete explicit small-cylinder classification**, not a new transfer-operator construction.

## References

1. W. Bahsoun and S. Vaienti, *Escape Rates Formulae and Metastability for Randomly Perturbed Maps*, arXiv:1206.3654, first public version June 16, 2012.
2. W. Bahsoun, J. Schmeling, and S. Vaienti, *On Transfer Operators and Maps with Random Holes*, arXiv:1405.0361, first public version May 2, 2014.
3. O. Georgiou, C. Dettmann, and E. Altmann, *Faster than expected escape for a class of fully chaotic maps*, arXiv:1207.7000, first public version July 2012.
