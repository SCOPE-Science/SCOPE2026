# Sharp twelve-versus-thirteen positivity threshold for exactly started BDF2 on complete-graph diffusion

## Finding

Let \(m\ge2\) be an integer, \(\lambda>0\), and \(h>0\). On the complete graph with uniform jump rates, write
\[
J_m=\frac1m\mathbf 1\mathbf 1^{\mathsf T},\qquad Q_m=-\lambda(I_m-J_m).
\]
For the implicit two-step backward differentiation formula (BDF2), define transition approximants by the exact semigroup start and the constant-step recurrence
\[
T_0=I_m,\qquad T_1=e^{hQ_m},\qquad
(3I_m-2hQ_m)T_k=4T_{k-1}-T_{k-2}\quad(k\ge2).
\]
**The sharp all-step classification is**
\[
\left[\ T_k\text{ is entrywise nonnegative for every }h>0\text{ and every integer }k\ge0\ \right]
\quad\Longleftrightarrow\quad m\le12.
\]
Every approximant has all row and column sums equal to one, regardless of positivity. For every \(m\ge13\), the second computed step already has negative diagonal entries when \(h\lambda=3\). Thus thirteen is the smallest state count producing a positivity violation within the uniform complete-graph family **with exact exponential initialization**.

The main scalar ingredient, proved below for all real \(s>0\), is the strict lower barrier
\[
-\frac1{11}<u_k(s)\le1\quad(k\ge0),\qquad
u_0=1,\quad u_1=e^{-s},\quad
u_k=\frac{4u_{k-1}-u_{k-2}}{3+2s}\quad(k\ge2),
\]
This scalar sequence is the nontrivial eigenvalue response of the numerical transition matrix.

## Assumptions and scope

The generator uses the row-convention continuous-time Markov convention: its off-diagonal rates are \(\lambda/m\), its diagonal entries equal \(-\lambda(m-1)/m\), and all row sums are zero. The graph has \(m\) vertices and uniform rates; no result is claimed for arbitrary weighted graphs or for inexact, backward-Euler, or Runge–Kutta starting steps. The quantified all-step property includes all positive stepsizes and unboundedly many time steps. Only matrix-entry positivity is at issue; no maximum-norm or total-variation preservation is asserted beyond what follows from a nonnegative stochastic matrix.

## Proof

**Reduction to one scalar response.** The complementary projectors \(J_m\) and \(I_m-J_m\) commute with the recurrence. Hence for \(s=h\lambda>0\),
\[
T_k=J_m+u_k(s)(I_m-J_m),\qquad
u_0=1,\qquad u_1=e^{-s},\qquad
u_k=\frac{4u_{k-1}-u_{k-2}}{D},\quad D=3+2s.
\]
The off-diagonal entries of \(T_k\) are \((1-u_k)/m\), and its diagonal entries are \((1+(m-1)u_k)/m\). Therefore
\[
T_k\ge0\text{ entrywise}\quad\Longleftrightarrow\quad
-\frac1{m-1}\le u_k\le1.
\]
The stochastic row and column sums are automatic.

**Positive-root regime.** If \(0<s<1/2\), the recurrence has roots
\[
r_\pm=\frac{2\pm\sqrt{1-2s}}{D},\qquad0<r_-<r_+<1.
\]
Let \(p(r)=Dr^2-4r+1\). A direct substitution gives
\[
p(e^{-s})=e^{-2s}\big(D-4e^s+e^{2s}\big)>0,
\]
since the bracket vanishes at zero and has derivative \(2(e^s-1)^2>0\). Also \(e^{-s}>e^{-1/2}>1/2\ge r_-\). Thus \(e^{-s}>r_+\). The root expansion of \(u_k\) has the form
\[
u_k=A r_+^k-C r_-^k,\qquad A=1+C>1,\ C>0.
\]
It is positive for every \(k\). Its first difference is negative because \(u_1<1\), and the ratio of the potentially positive second term in subsequent differences to the negative first term decays by \(r_-/r_+<1\); hence \(u_k\) decreases strictly and stays between zero and one. At \(s=1/2\), the repeated root yields
\[
u_k=2^{-k}\big[1+k(2e^{-1/2}-1)\big],
\]
which is again positive and strictly decreasing because \(0<2e^{-1/2}-1<1\).

**Oscillatory regime and tail bounds.** For \(s>1/2\), define \(\theta\) through \(\cos\theta=2/\sqrt D\), so \(0<\theta<\pi/2\). Direct solution of the recurrence yields
\[
u_k=D^{-k/2}\left[\cos(k\theta)+
\frac{De^{-s}-2}{\sqrt{D-4}}\sin(k\theta)\right].\tag{1}
\]
For \(1/2<s\le1\), the strictly decreasing function \((3+2s)e^{-s}\) lies between \(5/e\) and \(4e^{-1/2}\); the elementary bounds \(e<10/3\) and \(e^{1/2}>8/5\) give \(\lvert De^{-s}-2\rvert<1/2\). Since \(\lvert\sin(k\theta)\rvert\le k\sin\theta\) and \(D\ge4\), equation (1) implies
\[
\lvert u_k\rvert\le2^{-k}(1+k/4)\quad(k\ge0).
\]
For all \(k\ge5\), the right side is at most \(9/128<1/11\). For \(s\ge1\) we have \(D\ge5\) and \(0<De^{-s}<2\), so equation (1) gives
\[
\lvert u_k\rvert<\sqrt5\,5^{-k/2}\quad(k\ge0).
\]
For all \(k\ge4\), the latter is at most \(\sqrt5/25<1/11\). Both estimates also imply \(u_k<1\) for \(k\ge2\) in their respective ranges. Together with \(u_0=1\) and \(0<u_1<1\), only indices two through four remain for the negative lower bound.

**Exact low-index lower bounds.** Direct recurrence expansion gives
\[
\begin{aligned}
u_2&=\frac{4e^{-s}-1}{D},\\
u_3&=\frac{(16-D)e^{-s}-4}{D^2},\\
u_4&=\frac{(64-8D)e^{-s}+D-16}{D^3}.
\end{aligned}\tag{2}
\]
For \(u_2\), the inequality \(u_2>-1/11\) is equivalent to
\[
s+22e^{-s}-4>0.
\]
Its unique minimum is \(\log22-3>0\), since \(e^3<22\).

For \(u_3\), set \(H(D)=D^2-44+11(16-D)e^{-(D-3)/2}\). It suffices to prove \(H(D)>0\). If \(4\le D\le11/2\), the inequalities \(e^{-s}>1/4\), \(16-D\ge21/2\) and \(D^2-44\ge-28\) show
\[
H(D)>-28+\frac{231}{8}>0.
\]
If \(11/2\le D\le\sqrt{44}<20/3\), then \(s<11/6\), so \(e^{-s}>1/7\) and
\[
H(D)>-\frac{55}{4}+\frac{44}{3}>0.
\]
For \(\sqrt{44}\le D\le16\), equation (2) gives \(u_3\ge-4/D^2\ge-1/11\). For \(D\ge16\), the function \((D-16)e^{-(D-3)/2}\) has maximum \(2e^{-15/2}<1\) at \(D=18\); therefore \(u_3>-5/D^2\ge-5/256>-1/11\).

For \(u_4\), split the possible \(D\ge4\) into five intervals. If \(4\le D\le9/2\), then \(e^{-s}>2/5\) and the numerator in (2) exceeds \(-4/5\), whence \(u_4>-1/80\). If \(9/2\le D\le11/2\), then \(e^{-s}>1/4\) and the numerator exceeds \(-13/2\), whence \(u_4>-52/729\). If \(11/2\le D\le8\), the exponential term is nonnegative and the increasing function \((D-16)/D^3\) has minimum \(-84/1331\). If \(8\le D\le32\), then \(s\ge5/2\) and \(e^{-s}<1/12\), implying that the numerator exceeds \((D-32)/3\) and \(u_4>-1/64\). For \(D\ge32\) that numerator is nonnegative. Each of these negative comparison fractions is strictly greater than \(-1/11\). The exponential comparisons used here follow from the positive Taylor series, for example \(e^{5/2}>12\), \(e^{3/4}<5/2\), \(e^{5/4}<4\), and \(e^{11/6}<7\); rational enclosures appear in the accompanying checker.

The same oscillatory bounds already give \(u_2,u_3,u_4<1\), completing \(-1/11<u_k\le1\) for every \(s>0,k\ge0\).

**Sharp dimension obstruction.** If \(m\le12\), then \(-1/(m-1)\le-1/11\), so every entry of every \(T_k\) is nonnegative. If \(m\ge13\), set \(s=3\). Equation (2) gives
\[
u_2(3)=\frac{4e^{-3}-1}{9}<-\frac1{12},
\]
because \(e^3>16\). The diagonal \((1+(m-1)u_2(3))/m\) is then strictly negative. This proves both directions, including the endpoint \(m=12\) and the minimal counterexample \(m=13\). \(\square\)

## Verification

Run `python3 verify.py` with Python 3 (standard library only). It checks the scalar recurrence identities using exact rational coefficients of \(1\) and \(e^{-s}\), establishes rigorous rational Taylor bounds for the exponential inequalities and for the \(m=13\) witness, and performs 2,070,000 supplementary finite recurrence comparisons. Expected output starts with `VERIFY_OK`. These finite tests do not establish the infinite claim; the interval-based proof above does.

## Relationship to prior work

The general theory of monotonicity-preserving linear multistep methods and the importance of starting procedures are established by Hundsdorfer, Ruuth and Spiteri (2002 report; subsequently journal publication), especially the section on implicit second-order two-step schemes. Their results concern general monotonicity and boundedness under prescribed assumptions on the differential system, rather than this uniform complete-graph/exact-semigroup-start all-time dimension dichotomy. Hundsdorfer, Mozartova and Spijker (2010) analyze sharp general stepsize restrictions for boundedness and monotonicity; their generic coefficient tests are not this network-size classification. The explicit modal reduction used here is elementary; the claimed addition is the sharp twelve-versus-thirteen all-step positivity classification derived from it.

## Limitations

The proof covers only uniform-rate complete-graph generators and the exact semigroup first step. It does not characterize other graphs, uneven stationary probabilities, inexact start procedures, variable stepsizes, or positivity for all continuous-time generators of a given size. The dimension threshold is specific to simultaneous quantification over all positive stepsizes and every subsequent BDF2 step. No claim is made that the general modal reduction or the broader multistep positivity literature is new. Related analyses of multistep methods in symmetric Markov systems could contain an equivalent specialized conclusion under other terminology; independent scientific assessment has not been performed.

## References

1. W. Hundsdorfer, S. J. Ruuth and R. J. Spiteri, *Monotonicity-preserving linear multistep methods*, CWI report MAS-R0210, dated 30 April 2002, https://ir.cwi.nl/pub/4231/04231D.pdf; later SIAM Journal on Numerical Analysis 41 (2003), 605–623, DOI 10.1137/S0036142902406326.
2. W. Hundsdorfer, A. Mozartova and M. N. Spijker, *Stepsize Restrictions for Boundedness and Monotonicity of Multistep Methods*, CWI report (2010), https://ir.cwi.nl/pub/16707/16707B.pdf.
3. W. Hundsdorfer, *Partially implicit BDF2 blends for convection dominated flows*, CWI report (1998), https://ir.cwi.nl/pub/4596/04596D.pdf; comparison concerns alternative BDF2 use and starting treatments.
