# Sharp antitone dependence at the first repeated draw under unequal sampling

## Finding

Let \(m\ge2\), let \(p_1,\ldots,p_m>0\) sum to one, and let \(X_0,X_1,\ldots\) be independent draws from this categorical law. Write \(K=\min\{k\ge1:X_k\in\{X_0,\ldots,X_{k-1}\}\}\), let \(S\in\{0,\ldots,K-1\}\) be the unique position of the previous occurrence of \(X_K\), and set \(R=K-S\). Thus \(S\) is the pre-collision offset and \(R\) is the backward recurrence distance.

For \(1\le k\le m\), define
\[
q_k=(k-1)!\sum_{i=1}^m p_i^2 e_{k-1}(p_1,\ldots,\widehat p_i,\ldots,p_m),
\]
where \(e_r\) is the elementary symmetric polynomial and the hat means omission. The complete joint law is
\[
\Pr(S=s,R=r)=q_{s+r}\quad(s\ge0,\ r\ge1,\ s+r\le m),
\]
and is zero outside this triangular support. Its characteristic polynomial
\[
B(z)=\sum_{i=1}^m p_i^2\prod_{j\ne i}(1+p_jz)
\]
has only real strictly negative zeros. Consequently, for every integer \(2\le k\le m-1\),
\[
\boxed{q_k^2\ge\frac{m-k+1}{m-k}\,q_{k-1}q_{k+1}.}
\]
The coefficient is optimal simultaneously at all eligible indices: equality holds for uniform \(p\), and if \(m\ge3\), equality at even one eligible index forces all \(p_i\) equal.

Furthermore, the triangular array \(h(s,r)=\Pr(S=s,R=r)\) is reverse totally positive of order two:
\[
h(s,r)h(s',r')\le h(s,r')h(s',r)\quad(s<s',\ r<r').
\]
It is strict whenever all four corner probabilities are positive. Equivalently, as \(S\) increases, the conditional law of \(R\) decreases in the monotone likelihood-ratio order (with the customary ordered-support convention). In particular, for every two strictly increasing real functions \(\phi\) and \(\psi\) on the respective finite supports,
\[
\boxed{\operatorname{Cov}(\phi(S),\psi(R))<0.}
\]
For nondecreasing functions the covariance is nonpositive.

## Assumptions and scope

There are exactly \(m\) categories with strictly positive probabilities, independently sampled with replacement. The time indexing starts at zero; the first repeat index \(K\) lies in \(\{1,\ldots,m\}\). The earlier matching index \(S\) is well-defined because before time \(K\) all observed values are distinct. No ordering of categories and no restriction on their relative weights is imposed. The inequality involving three adjacent \(q\)'s is vacuous for \(m=2\); the reverse-TP2 and covariance assertions include that boundary case. Real-rootedness means all \(m-1\) zeros counted with multiplicity lie on the negative real axis.

## Proof

**Joint collision weights.** Fix \(K=k\), its earlier matching position \(S=s\), and the category \(i=X_k=X_s\). The remaining \(k-1\) prefix categories are distinct, omit \(i\), and can appear in any order. Summing their products gives \((k-1)!e_{k-1}(p_{-i})\). Multiplication by the two factors \(p_i\) at positions \(s\) and \(k\) and summation over \(i\) gives \(q_k\), independent of \(s\). Since \(R=k-s\), this proves the joint law. For each \(k\) there are exactly \(k\) positions \(s\), giving \(\Pr(K=k)=kq_k\), and the first-collision events partition probability one.

**Root interlacing.** Put \(P(z)=\prod_{j=1}^m(1+p_jz)\). Away from its zeros,
\[
\frac{B(z)}{P(z)}=\sum_{i=1}^m\frac{p_i^2}{1+p_iz}=\sum_{i=1}^m\frac{p_i}{z+1/p_i}.
\]
First suppose the masses are pairwise distinct. The poles \(-1/p_i\) are distinct and negative; between each two consecutive poles the displayed Stieltjes sum has derivative \(-\sum_i p_i/(z+1/p_i)^2<0\) and ranges from \(+\infty\) to \(-\infty\). Hence it has precisely one simple zero strictly between every consecutive pair. These are all \(m-1\) zeros of \(B\), since its leading coefficient is \(\prod_i p_i>0\). For repeated masses, approximate by distinct positive probability vectors. Polynomial coefficients and zeros converge continuously; thus every zero remains real and strictly negative (none can approach zero because \(B(0)=\sum_i p_i^2>0\)). More explicitly, when \(p\) takes \(d\) distinct values \(u_j\) of multiplicity \(n_j\), the polynomial contains each factor \((1+u_jz)^{n_j-1}\) and has \(d-1\) remaining simple zeros separating the distinct negative poles. If the \(p_i\) are not all equal and \(m\ge3\), this gives at least two distinct zeros. For the uniform law all zeros coincide.

**Sharp Newton bound.** Let \(b_r=[z^r]B(z)>0\), where \(0\le r\le m-1\). Real negative roots imply that \(b_r/\binom{m-1}{r}\) is log-concave by Newton's inequalities. Explicitly,
\[
\frac{b_r^2}{b_{r-1}b_{r+1}}\ge\frac{(r+1)(m-r)}{r(m-r-1)}\quad(1\le r\le m-2).
\]
As \(q_k=(k-1)!b_{k-1}\), substitution \(r=k-1\) and cancellation of factorials yields
\[
\frac{q_k^2}{q_{k-1}q_{k+1}}\ge\frac{m-k+1}{m-k}.
\]
For a positive-root-factorization, equality at an interior Newton inequality forces all linear factors to have the same root (the classical strict equality case of Newton/Maclaurin inequalities). The root description above makes this equivalent to uniform probabilities. Conversely the uniform law gives \(B(z)=mp^2(1+pz)^{m-1}\), hence equality. This also proves ordinary *strict* log-concavity of the \(q_k\)'s for every law, including the uniform law.

**Reverse-TP2 and negative regression.** The ratios \(q_{k+1}/q_k\) decrease strictly with \(k\). Thus for any \(s<s'\) and \(r<r'\) with all corners on the triangular support, repeated adjacent log-concavity gives \(q_{s+r}q_{s'+r'}<q_{s+r'}q_{s'+r}\). If the upper-right corner lies outside the support, its mass is zero, giving the non-strict comparison automatically. Therefore \(h\) is reverse-TP2. The conditional ratio
\[
\frac{\Pr(R=r\mid S=s')}{\Pr(R=r\mid S=s)}
\]
is decreasing on the common support as \(s<s'\), with any missing high values in the numerator assigned zero; this is the indicated monotone likelihood-ratio ordering.

Finally, for independent copies \((S,R)\), \((S',R')\), direct expansion yields
\[
\operatorname{Cov}(\phi(S),\psi(R))=
\sum_{s<s'}\sum_{r<r'}[\phi(s')-\phi(s)][\psi(r')-\psi(r)]
\bigl(h(s,r)h(s',r')-h(s,r')h(s',r)\bigr).
\]
Each bracket is nonpositive. The choice \(s=0,s'=1,r=1,r'=2\) has a strictly negative bracket for every \(m\ge2\): it is \(q_1q_3-q_2^2<0\) if \(m\ge3\), and \(-q_2^2<0\) if \(m=2\). Since all components have positive marginal probability, strictly increasing \(\phi,\psi\) make that term strictly negative. This proves the final assertion, including the boundary case.

## Verification

The standalone program `collision_verifier.py` uses exact rational arithmetic and *independently enumerates all ordered distinct prefixes and their closing repeated draw*. It compares those event probabilities with the generating-polynomial coefficients, tests the sharp Newton factor and equality cases, evaluates every rectangular reverse-TP2 determinant, and checks strict covariance. It passed 140 probability-vector instances with \(2\le m\le6\). Run `python3 collision_verifier.py` with Python 3. This is a finite consistency check; the general proof is the interlacing–Newton–reverse-TP2 argument above.

## Relationship to prior work

Camarri and Pitman (1998 technical report; 2000 journal article), Equation (1) and Section 3.1, give the exact unequal-probability first-repeat marginal \(\Pr(K=k)=k!\sum_{|A|=k}(\prod_{i\in A}p_i)(\sum_{i\in A}p_i)\). That equals \(kq_k\). The present law resolves the earlier matching position and backward distance and establishes their reverse-TP2 ordering. The marginal formula alone does not assert real-rootedness, the sharp Newton bound, or the sign/order property. Rathie and Zörnig (2003), Sections 1–2, examine unimodality of the uniform first-repeat distribution and later extensions, not the present general weighted two-variable ordering. Newton's inequalities and Stieltjes interlacing themselves are classical; the claim concerns their structural consequence for this birthday-collision dependence law.

## Limitations

This is a theorem about the **first** repeat, not later repeats, nonidentically distributed draws, or Markov-dependent samples. It assumes finite support with all masses positive; categories with zero weight may be deleted to recover this model. The general statement is mathematically proved here but has no independent mathematical audit. Historical priority cannot be certified exhaustively: Stein's 1990 technical report on Newton identities and generalized birthday problems was identified but its full text could not be obtained for direct comparison. Camarri and Pitman describe that work as deriving first-repeat approximation and error bounds, not the two-variable dependence classification. The accessible primary sources reviewed here do not establish the stated sharp ordering.

## References

1. M. Camarri and J. Pitman, *Limit distributions and random trees derived from the birthday problem with unequal probabilities*, University of California, Berkeley, Technical Report 523 (June 1, 1998); *Electronic Journal of Probability* **5** (2000), Paper 2, 1–18. DOI: `10.1214/EJP.v5-58`. Full text: `https://www.maths.tcd.ie/EMIS/journals/EJP-ECP/article/download/58/58-115-1-PB.pdf`.
2. P. N. Rathie and P. Zörnig, *On the birthday problem: some generalizations and applications*, *International Journal of Mathematics and Mathematical Sciences* **2003**, 3827–3840. DOI: `10.1155/S0161171203110101`.
3. C. Stein, *Application of Newton's Identities to a Generalized Birthday Problem and to the Poisson Binomial Distribution*, Stanford Department of Statistics Technical Report EFS NSF 354 (September 1990), `https://statistics.stanford.edu/technical-reports/application-newtons-identities-generalized-birthday-problem-and-poisson-binomial` (full text not inspected).
