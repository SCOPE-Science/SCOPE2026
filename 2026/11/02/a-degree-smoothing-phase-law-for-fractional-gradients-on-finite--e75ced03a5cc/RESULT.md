# A degree–smoothing phase law for fractional gradients on finite stars

## Finding

Let \(S_m\) be the unit-edge star with one center and \(m\ge2\) leaves. Let \(B\) be its leaf-minus-center oriented incidence map, \(L=B^{\mathsf T}B\) its combinatorial Laplacian, and \(T_{s,m}=BL^{-s}\) for \(s>0\), where the inverse power acts as zero on constants. All spaces carry ordinary, **unnormalized counting-measure** real \(\ell^p\) norms, including the \(m\)-edge output space.

Put \(a=(m+1)^{-s}\). For a vertex signal \((c,x_1,\ldots,x_m)\), with \(\bar x=m^{-1}\sum_i x_i\),
\[
 (T_{s,m}(c,x))_i=x_i-\bar x+a(\bar x-c).
\]
In particular, the exact endpoint and Hilbert norms, for every integer \(m\ge2\) and \(s>0\), are
\[
\begin{aligned}
\|T_{s,m}\|_{\ell^1\to\ell^1}&=\max\left\{ma,\ 2-\frac2m-\frac{m-2}{m}a\right\},\\
\|T_{s,m}\|_{\ell^2\to\ell^2}&=\max\{1,(m+1)^{1/2-s}\},\\
\|T_{s,m}\|_{\ell^\infty\to\ell^\infty}&=2-\frac2m+\frac{2a}{m}.
\end{aligned}
\]
The maximizing \(\ell^1\) input changes from a hub point mass to a leaf point mass at the exact crossover \(a=2/(m+2)\).

For each fixed \(1\le p<\infty\), \(s>0\), define the classical centered-moment constant \(C_p=\|I-E\|_{L^p(0,1)\to L^p(0,1)}\), where \(Ef=\int_0^1f\). Then there is a sharp degree–smoothing phase line:
\[
\begin{cases}
\displaystyle\lim_{m\to\infty}m^{s-1/p}\|T_{s,m}\|_{p\to p}=1,&0<s<1/p,\\[3pt]
\displaystyle\lim_{m\to\infty}\|T_{s,m}\|_{p\to p}=D_p,&s=1/p,\\[3pt]
\displaystyle\lim_{m\to\infty}\|T_{s,m}\|_{p\to p}=C_p,&s>1/p.
\end{cases}
\]
At the critical line the exact universal limiting constant is the operator norm
\[
 D_p=\sup_{(c,f)\ne(0,0)}
 \frac{\|f-Ef-c\|_{L^p(0,1)}}{\bigl(|c|^p+\|f\|_{L^p(0,1)}^p\bigr)^{1/p}}.
\]
One has \(D_1=C_1=2\), \(D_2=C_2=1\), and, for every \(1<p<\infty\) with \(p\ne2\), the **strict critical resonance** \(D_p>C_p>1\). For \(1<p<\infty\) the already-known Franchetti/centered-moment constant can be evaluated by
\[
 C_p=\max_{0<t<1}\bigl[t^{p-1}+(1-t)^{p-1}\bigr]^{1/p}
 \bigl[t^{1/(p-1)}+(1-t)^{1/(p-1)}\bigr]^{1-1/p};
\]
this known formula, by itself, is not a new result. In particular the ordinary incidence Riesz transform \(BL^{-1/2}\) has \(\|BL^{-1/2}\|_{1\to1}=m/\sqrt{m+1}\), \(\|BL^{-1/2}\|_{2\to2}=1\), and \(\|BL^{-1/2}\|_{\infty\to\infty}=2-2/m+2/[m\sqrt{m+1}]\).

## Assumptions and scope

The vertex set consists of hub \(0\) and leaves \(1,\dots,m\). Fix the orientation \(Bf=(f_i-f_0)_{i=1}^m\); all norms use unweighted counting measure. \(L^{-s}\) is defined by the real spectral calculus with eigenvalue zero at eigenvalue zero; no inverse on constants is asserted. The full theorem is about real \(\ell^p\) operator norms and fixed \(p,s\) while \(m\) grows. The critical limiting variational constant \(D_p\) is specified exactly as a Banach-space operator norm; no elementary closed expression for its numerical value is claimed when \(p\ne1,2\).

## Proof

**Spectral decomposition and exact endpoints.** Decompose any leaf vector as \(x=(x-\bar x\mathbf1)+\bar x\mathbf1\). The star Laplacian is zero on constants, equals identity on the \((m-1)\)-dimensional leaf-fluctuation space (hub coordinate zero, leaf sum zero), and has eigenvalue \(m+1\) on the radial line spanned by \((-m,1,\ldots,1)\). The incidence map sends the first space identically to leaf fluctuations and sends the radial part to the constant edge vector. Consequently \(T_{s,m}(c,x)=(x-\bar x\mathbf1)+a(\bar x-c)\mathbf1\), without approximation. Its matrix has hub-column entries \(-a\), leaf diagonal entries \(1-(1-a)/m\), and off-diagonal leaf entries \(-(1-a)/m\). All \(a\) lie in \((0,1)\). The maximum column sum of absolute entries is \(\max\{ma,2-2/m-(m-2)a/m\}\); the maximum row sum is \(2-2/m+2a/m\). Comparing the two column sums gives precisely \(a=2/(m+2)\). In Hilbert norm the squared singular values are \(1\) on leaf-fluctuations and \((m+1)a^2\) on the radial line, proving the third stated exact norm.

**Asymptotic decomposition.** Write \(E_m x=(m^{-1}\sum_i x_i)\mathbf1\) and \(J_m c=c\mathbf1\). Then \(T_{s,m}(c,x)=(I-E_m)x+a(E_mx-J_mc)\). The centered part has uniformly bounded \(\ell^p\) norm (at most \(2\)), while \(\|aJ_m\|=am^{1/p}\) and \(\|aE_m\|=a\). Thus for \(s<1/p\), the hub-coordinate test gives the matching lower bound \(am^{1/p}\), and the triangle inequality gives \(\|T_{s,m}\|\le2+a+am^{1/p}\), proving the first branch. If \(s>1/p\), the perturbation \(a(E_m-J_m)\) has norm at most \(a+am^{1/p}\to0\), and the star norm approaches the norm of \(I-E_m\). Identify \(\ell^p_m\) with step functions on \([0,1]\) having intervals of measure \(1/m\) (a common scalar rescaling cancels from an operator norm). The norms of these restricted centered operators converge to \(C_p=\|I-E\|_{L^p}\), by conditional-expectation approximation of arbitrary \(L^p\) functions and boundedness of \(I-E\). This proves the third branch. For \(p=1\) the exact formula directly yields \(C_1=2\).

**The critical operator.** For a step function \(f\) with value \(f_i\) on each of \(m\) equal intervals, set \(x_i=m^{-1/p}f_i\). Then the input norm of \((c,x)\) equals the \(\mathbb R\oplus_p L^p\) norm of \((c,f)\). After multiplying each output edge coordinate by \(m^{1/p}\), its step-function representation is
\[
 f-Ef+(m+1)^{-1/p}Ef-\left(\frac{m}{m+1}\right)^{1/p}c.
\]
The difference from \(f-Ef-c\) tends to zero in operator norm: its bound is \((m+1)^{-1/p}+1-(m/(m+1))^{1/p}\). The step subspaces are dense in \(L^p(0,1)\) for \(p<\infty\), so the norms of the restrictions converge to the full operator norm \(D_p\). This establishes the second branch without relying on finite enumeration. At \(p=2\), the orthogonal decomposition into constants and mean-zero functions gives \(\|f-Ef-c\|_2^2=\|f-Ef\|_2^2+|c|^2\le\|f\|_2^2+|c|^2\), with equality for a nonzero centered \(f\); hence \(D_2=1\). At \(p=1\), the exact column sums at \(s=1\) converge to \(2\), so \(D_1=2\).

**Strict critical resonance for non-Hilbert exponents.** For \(1<p<\infty\), the classical sharp formula for \(C_p\) above has an extremal two-valued test at some proportion \(t\in(0,1)\). The known strict inequality \(C_p>1\) for \(p\ne2\) forces \(t\ne1/2\) (at \(t=1/2\) the displayed formula is \(1\)). Choose the optimal two-valued input \(f\) for that proportion, and write \(u=f-Ef\). The two output values of \(u\) are nonzero and have opposite signs with magnitudes proportional to \(1-t\) and \(t\). Direct substitution gives
\[
 \int_0^1|u|^{p-2}u\,dx\ne0
 \quad\text{when }t\ne1/2\text{ and }p\ne2.
\]
The derivative of \(\|u-c\|_p^p\) at \(c=0\) is \(-p\int|u|^{p-2}u\), which is nonzero, while the denominator \(\|f\|_p^p+|c|^p\) changes by \(o(|c|)\). Choosing the sign of a sufficiently small \(c\) therefore strictly increases the ratio above the already-attained \(C_p\). This proves \(D_p>C_p\) for every \(p\ne2\). All limiting statements concern fixed \(s,p\) and the family of finite stars as \(m\to\infty\).

## Verification

The accompanying Python checker independently diagonalizes the finite-star Laplacian numerically for seven leaf counts and seven positive smoothing exponents, checks all three exact endpoint formulae using matrix norms/SVD, tests the variational critical-resonance witnesses for seven non-Hilbert exponents, and compares the critical step-function construction at finite leaf counts. It is a supplementary finite diagnostic, **not** a proof of the infinite limiting claims. Run `python proof_checks.py` with the versions in `requirements.txt`; the proof above contains the general arguments.

## Relationship to prior work

Levi et al. (2021) and Martini et al. (2023) study Riesz transforms for flow Laplacians on **infinite** homogeneous and nonhomogeneous trees, respectively, with weighted measures and no finite-star hub/leaf concentration. Their tree results motivate scrutiny of graph Riesz norms but do not imply the unweighted finite-star degree–smoothing phase law. The sharp constant \(C_p\) for centering is classical and is explained, with an explicit formula, by Shargorodsky and Sharia (2022); it is explicitly not claimed as novel here. The new claim concerns the coupling of the center coordinate to leaf centering at \(s=1/p\), the strict critical limit, and the all-\(s\) exact endpoint norms. The standard star-Laplacian spectral decomposition or pseudoinverse itself is not claimed as new.

## Limitations

No general-tree estimate, result for weighted stars, normalized vertex measures, general fractional graph filters, or closed elementary formula for \(D_p\) when \(p\ne1,2\) is asserted. The strong \(\ell^p\) counts should not be conflated with weak-type Riesz estimates under degree-normalized measures. The existence of older exact star-pseudoinverse identities means formula-level historical priority requires further independent review; a relevant 2017 network-pseudoinverse article could not be checked in full text. No independent mathematical audit has been performed.

## References

1. G. Levi, M. Martini, F. Santagati, A. Tabacco, M. Vallarino, *Riesz transform for a flow Laplacian on homogeneous trees*, arXiv:2107.06620v1, first posted 2021-07-14. https://arxiv.org/abs/2107.06620
2. E. Shargorodsky and F. Sharia, *Sharp estimates for conditionally centered moments and for compact operators on Lp spaces*, Mathematische Nachrichten, https://doi.org/10.1002/mana.202100217 (public online 2022-12-18).
3. A. Martini, F. Santagati, A. Tabacco, M. Vallarino, *Riesz transform and spectral multipliers for the flow Laplacian on nonhomogeneous trees*, arXiv:2310.09113v1, first posted 2023-10-13. https://arxiv.org/abs/2310.09113
4. P. Van Mieghem, K. Devriendt, H. Cetinay, *Pseudoinverse of Laplacian and best spreader node in a network*, Physical Review E 96 (2017), article 032311; comparison to complete source remains incomplete. https://repository.tudelft.nl/record/uuid:d30bd7b7-808c-4594-ab34-be90b434fa53
