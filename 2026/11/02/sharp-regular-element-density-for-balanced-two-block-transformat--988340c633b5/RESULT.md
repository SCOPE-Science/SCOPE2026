# Sharp regular-element density for balanced two-block transformation monoids

## Finding

Let \(m\geq 1\), let \(X=A\sqcup B\) with \(|A|=|B|=m\), and write \(T_m\) for the monoid of all selfmaps of \(X\) that send each of \(A,B\) wholly into one of these two blocks. An element \(f\in T_m\) is *regular* if some \(g\in T_m\) satisfies \(fgf=f\), with the convention that compositions act on the right. Let \(R_m\) be the proportion of regular elements of \(T_m\), and let \(\left\{\begin{smallmatrix}m\\s\end{smallmatrix}\right\}\) denote a Stirling number of the second kind.

For every integer \(m\geq1\), the exact proportion is
\[
R_m=\frac12+\frac{1}{m^{2m}}\sum_{s=1}^{m}\binom ms\,s!\left\{\begin{matrix}m\\s\end{matrix}\right\}s^m
-\frac{1}{2m^{2m}}\sum_{s=1}^{m}\binom ms\left(s!\left\{\begin{matrix}m\\s\end{matrix}\right\}\right)^2.
\]

There is also a sharp asymptotic, including its leading constant:
\[
\boxed{R_m=\frac12+C\rho^m(1+o(1)),\qquad m\longrightarrow\infty.}
\]
To define the constants unambiguously, let \(x\) be the unique root in \((0,1)\) of
\[
\exp\!\left(-\frac{x}{1-e^{-x}}\right)=1+(x-1)e^x,
\]
put \(y=x/(1-e^{-x})\), and set
\[
\rho=\frac{1+(e^x-1)e^y}{e^2xy},\qquad
C=\frac{1}{\sqrt{xy-(y-1)^2}}.
\]
Numerically, \(x=0.594672306785008\ldots\), \(y=1.326633507659143\ldots\), \(\rho=0.696742956572524\ldots\), and \(C=1.210700991285293\ldots\). Thus the regular proportion tends to \(1/2\) from above at an explicitly determined exponential rate.

## Assumptions and scope

Both blocks are nonempty, finite, labeled subsets of equal size; there are no injectivity, surjectivity, or idempotence assumptions on the transformations. We count *regular elements*, not idempotents, units, or abstract isomorphism classes. The statement includes \(m=1\). It does not assert the same asymptotic for unequal block sizes or for more than two blocks. The notation \(o(1)\) is relative to the correction \(C\rho^m\), not relative to \(R_m\).

## Proof

**1. Reduction to two image sets.** Every \(f\in T_m\) determines a character \(\chi_f:\{A,B\}\to\{A,B\}\), recording the target block of each source block. There are four characters; for each, the restrictions of \(f\) are independent maps from \(m\) points to \(m\) points, so \(|T_m|=4m^{2m}\).

If \(\chi_f\) is bijective, \(f\) is regular: select one preimage for each point in each nonempty restriction image, define \(g\) on the two target blocks using these selections, and extend arbitrarily within the required opposite source blocks. Then \(g\) preserves the two-block partition and \(fgf=f\).

Suppose instead that both source blocks map into the same target block, say \(A\). Write \(U=f(A)\) and \(V=f(B)\); both are nonempty subsets of \(A\). If \(fgf=f\), then \(g\) sends the entire target block \(A\) into either \(A\) or \(B\). Since every \(z\in U\cup V\) satisfies \(z=(zg)f\), one of \(f(A),f(B)\) must equal \(U\cup V\). Hence \(U\subseteq V\) or \(V\subseteq U\). Conversely, when (say) \(V\subseteq U\), choose within \(A\) a preimage of every \(z\in U\); define \(g\) on \(A\) to realize these choices and extend it arbitrarily on all other points while preserving the partition. This yields \(fgf=f\). Thus for either constant character regularity is equivalent to the two restriction images being comparable by inclusion.

Let \(F,G\) be independent uniform functions from an \(m\)-element set to itself. Put \(a_m=\Pr(\operatorname{im}G\subseteq\operatorname{im}F)\), \(b_m=\Pr(\operatorname{im}G=\operatorname{im}F)\). Inclusion-exclusion gives the comparable-image probability \(2a_m-b_m\), and the two bijective characters constitute exactly half of \(T_m\). Therefore
\[
R_m=\frac12+a_m-\frac{b_m}{2}.
\]

**2. Exact enumeration.** If the image of \(F\) has size \(s\), the number of possible functions \(F\) is \(\binom ms s!\left\{\begin{smallmatrix}m\\s\end{smallmatrix}\right\}\). For each such \(F\), exactly \(s^m\) functions \(G\) have image inside its image. Likewise, requiring the two images to be the same \(s\)-set gives \(\binom ms(s!\left\{\begin{smallmatrix}m\\s\end{smallmatrix}\right\})^2\) ordered pairs. Consequently
\[
a_m=\frac{\sum_{s=1}^m\binom ms s!\left\{\begin{smallmatrix}m\\s\end{smallmatrix}\right\}s^m}{m^{2m}},\quad
b_m=\frac{\sum_{s=1}^m\binom ms(s!\left\{\begin{smallmatrix}m\\s\end{smallmatrix}\right\})^2}{m^{2m}}.
\]
Substitution proves the exact formula.

**3. Exponential generating function and unique saddle.** In a pair of functions, let \(u\) and \(v\) be the respective numbers of inputs that land at a fixed target point. Image inclusion means \(u=0\) implies \(v=0\). The exponential generating function for admissible occupancies at one target point is
\[
H(z,w)=1+(e^z-1)e^w.
\]
As both functions have \(m\) labeled inputs and \(m\) possible output points,
\[
a_m=\frac{(m!)^2}{m^{2m}}[z^mw^m]H(z,w)^m.
\]
The positive saddle equations are \(xH_z(x,y)/H(x,y)=1\) and \(yH_w(x,y)/H(x,y)=1\). They reduce to \(y=x/(1-e^{-x})\) and \(e^{-y}=1+(x-1)e^x\). The left side of the latter equation decreases strictly with \(x>0\); the right side increases strictly because its derivative is \(xe^x\). At \(x\downarrow0\), the respective limits are \(e^{-1}\) and \(0\), while at \(x=1\) they are less than \(1\) and equal to \(1\). Hence there is exactly one solution in \((0,1)\).

**4. Two-dimensional local limit at the saddle.** Define an integer-valued random vector \((U,V)\) by
\[
\Pr(U=u,V=v)=\frac{x^uy^v}{u!v!H(x,y)}
\]
for \((u,v)=(0,0)\) and for \(u\geq1,v\geq0\), with probability zero otherwise. This is a probability distribution whose mean is \((1,1)\). Differentiating \(H\) and using the saddle equations gives covariance matrix
\[
\Sigma=\begin{pmatrix}x&y-1\\y-1&y\end{pmatrix},\qquad D=\det\Sigma=xy-(y-1)^2>0.
\]
Positivity follows also from the positive probabilities at \((0,0),(1,0),(1,1)\), which are not collinear. These three support points generate the full difference lattice \(\mathbb Z^2\). Moreover the distribution has finite exponential moments. Consequently the lattice local central limit estimate is
\[
\Pr\!\left(\sum_{j=1}^m(U_j,V_j)=(m,m)\right)
=\frac{1+o(1)}{2\pi m\sqrt D},
\]
for independent copies. For completeness, Fourier inversion proves this estimate: the characteristic function has modulus strictly below \(1\) away from the origin on the two-dimensional torus because of the full difference lattice; near the origin, after subtracting its mean, its logarithm is \(-\tfrac12t^{\mathsf T}\Sigma t+O(\lVert t\rVert^3)\). Splitting the integral into a shrinking neighborhood and its complement, rescaling \(t\) by \(m^{-1/2}\), and integrating the resulting Gaussian yields exactly the displayed constant, with no lattice-period multiplier.

Under this tilted law, coefficient extraction becomes
\[
a_m=\frac{(m!)^2}{m^{2m}}\left(\frac{H(x,y)}{xy}\right)^m
\Pr\!\left(\sum_{j=1}^m(U_j,V_j)=(m,m)\right).
\]
Stirling's formula therefore implies
\[
a_m\sim\frac{1}{\sqrt D}\left(\frac{H(x,y)}{e^2xy}\right)^m=C\rho^m.
\]

**5. The equal-image overlap is negligible.** With the same tilted distribution, the probability of a point occupied by \(F\) but not by \(G\) is \(p=(e^x-1)/H(x,y)>0\). Conditional on the two total occupancies being \(m\), equal images require that none of the \(m\) output points have such an occupancy. Thus, using the local limit denominator from step 4,
\[
\frac{b_m}{a_m}
\leq\frac{(1-p)^m}{\Pr(\sum_{j=1}^m(U_j,V_j)=(m,m))}
=O\!\left(m(1-p)^m\right)=o(1).
\]
Combining \(R_m=1/2+a_m-b_m/2\) with \(a_m\sim C\rho^m\) proves the claimed sharp asymptotic. In particular \(0<\rho<1\), as witnessed by the root formula or the strict exponential rate of the local occupancy event.

## Verification

The standalone file `verify_regular_bipartition.py` is a standard-library-only Python 3 program. It constructs every partition-preserving map for \(m=1,2,3\) and tests regularity by explicit composition over *all* proposed inner inverses. The verified regular counts are \(4\) of \(4\), \(60\) of \(64\), and \(2400\) of \(2916\), respectively. A separate Stirling recursion checks the exact formula through \(m=12\) and its agreement with the saddle correction at \(m=40\) and \(m=80\). The finite checks do not establish the infinite asymptotic; the proof above does.

Run from the directory containing the file:

```text
python3 verify_regular_bipartition.py
```

The successful verifier terminates with `VERIFY_OK`.

## Relationship to prior work

Sarkar and Singh [1], especially Proposition 3.4 and Theorem 3.5, establish qualitative regularity criteria for the broader class of partition-preserving transformation semigroups. The image-containment reduction in step 1 is an explicit two-equal-block specialization of that established structural framework; it is not claimed as a novel general criterion. The contribution assessed here is the exact *regular-element proportion* and its sharp exponential correction, including an explicit saddle point and prefactor. Sarkar and Singh [2] enumerate regular elements of a different subsemigroup, one in which each source block maps *onto* an entire target block, while Dolinka, East, and Mitchell [3] classify idempotents and idempotent generators. Neither of those enumerations implies the present regular-element density without an additional image-comparison count and asymptotic analysis. The possibility of equivalent statements in other occupancy or partition-semigroup literature remains a priority risk.

## Limitations

The theorem applies only to a pair of equal-sized nonempty blocks and to ordinary total transformations preserving this partition. The proof of the leading constant uses the two-dimensional lattice local central limit argument stated explicitly above. The provided verifier exhausts only \(m\leq3\) for direct regularity and checks exact formulas at larger finite \(m\); it is corroborating computation rather than a substitute for the asymptotic proof. The originality assessment is restricted to the sources described in the accompanying review and should not be interpreted as a comprehensive publication-priority certification.

## References

1. M. Sarkar and S. N. Singh, *Semigroups of transformations whose characters belong to a given semigroup*, arXiv:2310.19414v1, publicly posted 30 October 2023, especially Proposition 3.4 and Theorem 3.5. https://arxiv.org/abs/2310.19414
2. M. Sarkar and S. N. Singh, *Regular, Unit-regular, and Idempotent elements of semigroups of transformations that preserve a partition*, arXiv:2010.14033v1, 27 October 2020, especially Sections 3 and 6. https://arxiv.org/abs/2010.14033
3. I. Dolinka, J. East, and J. D. Mitchell, *Idempotent rank in the endomorphism monoid of a non-uniform partition*, arXiv:1504.02520v1, 9 April 2015, especially Section 3. https://arxiv.org/abs/1504.02520
