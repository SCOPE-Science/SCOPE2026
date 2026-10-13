# Exact nested extremality windows for the mixed-spin Ising disordered phase

## Finding
For the disordered translation-invariant splitting Gibbs measure in the mixed spin-\\((1,1/2)\\) Ising model of Akın and Mukhamedov, let \\(k\\ge 2\\) be the Cayley-tree order and let \\(f_k(\\theta)=k\\kappa(\\theta,k)^2-1\\) denote the function in their extremality condition. Define
\\[
x=\\frac{\\theta+\\theta^{{-1}}}{2}\\ge 1.
\\]
Then
\\[
f_k(\\theta)=\\frac{{H_k(x)}}{{1+2x^{{k+1}}}},
\\qquad
H_k(x)=2(k-1)x^{{k+1}}-2kx^{{k-1}}-1.
\\]
For every integer \\(k\\ge2\\), the polynomial \\(H_k\\) has a unique root \\(x_k>1\\). Consequently \\(f_k\\) has exactly two positive roots,
\\[
\\theta_k^-=x_k-\\sqrt{{x_k^2-1}},
\\qquad
\\theta_k^+=x_k+\\sqrt{{x_k^2-1}},
\\qquad
\\theta_k^-\\theta_k^+=1.
\\]
The source's sufficient extremality criterion \\(f_k(\\theta)<0\\) holds exactly when
\\[
\\theta_k^-<\\theta<\\theta_k^+.
\\]
Moreover these intervals strictly shrink with tree order:
\\[
(\\theta_{{k+1}}^-,\\theta_{{k+1}}^+)\\subsetneq(\\theta_k^-,\\theta_k^+)
\\qquad(k\\ge2).
\\]
This proves the all-order existence and strict-narrowing content of Conjecture 1 in the motivating paper.

## Assumptions and scope
The parameter satisfies \\(\\theta>0\\), and \\(k\\) is an integer with \\(k\\ge2\\). The argument concerns the specific disordered phase and the sufficient extremality condition derived in the source from the tree-indexed Markov-chain contraction estimate. It does not assert that failure of this sufficient condition proves non-extremality. The equality endpoints are not classified here.

## Proof
The source gives
\\[
f_k(\\theta)+1=
\\frac{{k(1+\\theta^2)^{{k-1}}(\\theta^2-1)^2}}
{{2^k\\theta^{{k+1}}+(1+\\theta^2)^{{k+1}}}}.
\\]
With \\(x=(\\theta+\\theta^{{-1}})/2\\), the identities \\(1+\\theta^2=2\\theta x\\) and \\((\\theta^2-1)^2=4\\theta^2(x^2-1)\\) give
\\[
f_k(\\theta)+1=
\\frac{{2k x^{{k-1}}(x^2-1)}}{{1+2x^{{k+1}}}}.
\\]
Subtracting one proves the stated reduction to \\(H_k\\).

For \\(x\\ge1\\),
\\[
H_k'(x)=2(k-1)x^{{k-2}}\\bigl((k+1)x^2-k\\bigr)>0.
\\]
Also \\(H_k(1)=-3\\) and \\(H_k(x)\\to+\\infty\\) as \\(x\\to+\\infty\\). Hence there is exactly one \\(x_k>1\\) with \\(H_k(x_k)=0\\). Since \\(\\theta\\mapsto(\\theta+\\theta^{{-1}})/2\\) maps positive \\(\\theta\\) onto \\([1,\\infty)\\), with reciprocal preimages away from \\(x=1\\), the two positive roots of \\(f_k\\) are exactly \\(\\theta_k^-\\) and \\(\\theta_k^+\\). Monotonicity of \\(H_k\\) gives \\(f_k(\\theta)<0\\) precisely when \\(x<x_k\\), which is equivalent to \\(\\theta_k^-<\\theta<\\theta_k^+\\).

It remains to prove strict nesting. At \\(x=x_k\\), write
\\[
A=(k-1)x_k^2-k.
\\]
The root equation gives \\(2x_k^{{k-1}}A=1\\), so \\(A>0\\). Set \\(B=kx_k^2-(k+1)=A+(x_k^2-1)\\). Then \\(B>A>0\\), and
\\[
H_{{k+1}}(x_k)+1=2x_k^kB
=x_k\\frac{{B}}{{A}}>1.
\\]
Thus \\(H_{{k+1}}(x_k)>0\\). Since \\(H_{{k+1}}(1)=-3\\) and \\(H_{{k+1}}\\) is strictly increasing, its unique root obeys \\(x_{{k+1}}<x_k\\). The function \\(x-\\sqrt{{x^2-1}}\\) is strictly decreasing for \\(x>1\\), while \\(x+\\sqrt{{x^2-1}}\\) is strictly increasing. Therefore \\(\\theta_{{k+1}}^->\\theta_k^-\\) and \\(\\theta_{{k+1}}^+<\\theta_k^+\\), proving strict interval inclusion.

## Verification
A standalone verifier checks the reduction identity exactly over rational test values, reconstructs the two critical roots by bisection for representative orders, recovers the source values \\(\\theta_3^-\\approx0.4779773475\\), \\(\\theta_3^+\\approx2.0921493567\\), \\(\\theta_4^-\\approx0.5398332572\\), and \\(\\theta_4^+\\approx1.8524238487\\), and checks strict nesting through \\(k=200\\). These finite checks corroborate the analytic proof and are not used as an infinite-order certificate.

## Relationship to prior work
Akın and Mukhamedov derive the all-order criterion and prove the \\(k=3\\) interval exactly. For \\(k=4\\) they obtain the two roots numerically using Mathematica. Their Conjecture 1 then states the all-order two-root extremality interval and nesting property, supported by plots for selected orders. The present reduction proves that conjectural root structure and strict narrowing in closed one-variable form.

A later paper by Qawasmeh, Mukhamedov, and Akın studies a different two-interaction \\((1,1/2)\\)-mixed Ising model on \\((m,k)\\)-ary trees. Its extremality theorem uses two interaction parameters and a cubic discriminant condition; it does not imply the reciprocal one-parameter root formula or the strict nesting result above.

## Limitations
The result concerns the sufficient extremality window singled out by the source. It does not identify the exact extremal/non-extremal boundary if the source's sufficient and Kesten--Stigum conditions leave a gap, does not classify endpoint equality, and does not address the later two-interaction \\((m,k)\\)-ary model except for literature comparison.

## References
1. H. Akın and F. Mukhamedov, *The extremality of disordered phases for the mixed spin-(1,1/2) Ising model on a Cayley tree of arbitrary order*, preprint posted 6 February 2023, doi:10.22541/au.167570700.04920927/v1; journal version, *Journal of Statistical Mechanics: Theory and Experiment* (2024) 013207, doi:10.1088/1742-5468/ad1be2.
2. A. Qawasmeh, F. Mukhamedov, and H. Akın, *Analysis of Gibbs Measures and Stability of Dynamical System Linked to (1,1/2)-Mixed Ising Model on (m,k)-Ary Trees*, *Mathematical Physics, Analysis and Geometry* 28 (2025), Article 10, doi:10.1007/s11040-025-09504-4.
