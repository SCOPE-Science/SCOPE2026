# Sharp five-state positivity barrier and reentrant timestep window for TR-BDF2 on directed cycles

## Finding

For every integer \(n\ge 2\), let \(S_n\) be the forward cyclic permutation matrix, defined by \((S_n)_{i,j}=1\) exactly when \(j\equiv i+1\pmod n\), and let \(Q_n=S_n-I\). Thus \(Q_n\) is the unit-rate continuous-time Markov generator of a directed \(n\)-cycle. Apply the standard L-stable TR-BDF2 endpoint rule, with stability function
\[
R(z)=\frac{1+(\sqrt2-1)z}{\bigl(1-(1-1/\sqrt2)z\bigr)^2},\qquad P_n(h)=R(hQ_n).
\]
Here \(P_n(h)\) is defined by the rational matrix functional calculus and \(h\ge0\). Its row sums are always one.

Set
\[
c=1-\frac1{\sqrt2},\quad \beta=\sqrt2-1,\quad \gamma=2-\sqrt2,\quad t=\frac{ch}{1+ch},
\]
and, for \(n\ge2\), define the polynomial
\[
q_n(t)=\beta-\gamma\sum_{j=1}^{n-1}t^j+(n-1)t^n.
\]
The following classification is exact:

1. For \(2\le n\le4\), the endpoint matrix is entrywise nonnegative for **every** \(h\ge0\), and is strictly positive entrywise for \(h>0\).
2. For each \(n\ge5\), the polynomial \(q_n\) has **exactly two** roots \(0<t_n^-<t_n^+<1\). With
\[
h_n^\pm=\frac{t_n^\pm}{c(1-t_n^\pm)},
\]
the full nonnegativity set is
\[
\boxed{\{h\ge0:P_n(h)\ge0\ \text{entrywise}\}=[0,h_n^-]\cup[h_n^+,\infty).}
\]
Every \(h\) in the open interval \((h_n^-,h_n^+)\) gives a negative diagonal entry; outside that interval all off-diagonal entries are strictly positive whenever \(h>0\). At either positive threshold the diagonal entries vanish and the off-diagonal entries remain strictly positive.
3. The roots and timestep thresholds satisfy the asymptotic laws
\[
\boxed{h_n^-\longrightarrow 1+\sqrt2,\qquad \frac{h_n^+}{n}\longrightarrow\frac1{cs_*}=3.4529561713\ldots,}
\]
where \(s_*>0\) is the unique solution of \(s_*/(e^{s_*}-1)=2-\sqrt2\). In particular, the last positivity-recovery step grows linearly with the number of states, while the first loss threshold approaches the classical absolute-monotonicity radius.

For the first unsafe dimension \(n=5\), the two thresholds are approximately \(h_5^-=3.222709632051\) and \(h_5^+=6.805854390690\). These decimals illustrate, rather than define, the exact algebraic boundaries.

## Assumptions and scope

The matrix \(S_n\) is a single directed unit-rate cycle; the rate and timestep can be rescaled together if the common rate is changed. No reversibility is assumed. The endpoints are those of unmodified L-stable TR-BDF2 with parameter \(2-\sqrt2\), not a hybrid, clipped, adaptively modified, or stagewise positivity-enforced version. “Nonnegative” refers to every entry of the **endpoint** matrix \(P_n(h)\). The theorem does not claim positivity of intermediate Runge–Kutta stages or positivity for general generators.

The method is second-order accurate and its scalar stability function agrees with equation (3.2) of Bonaventura and Della Rocca (2015), specialized to the L-stable parameter. All asserted inequalities include the boundary values, with \(P_n(0)=I\).

## Proof

**1. Resolvent representation.** Define \(T=(I-chQ_n)^{-1}\). From
\[
chQ_n=I-T^{-1},\qquad \frac{\beta}{c}=\sqrt2,
\]
we obtain the exact identity
\[
P_n(h)=(I+\beta hQ_n)T^2=(1+\sqrt2)T^2-\sqrt2T.
\]
For \(h>0\), set \(t=ch/(1+ch)\in(0,1)\). Since \(S_n^n=I\), the convergent geometric series gives
\[
T=(1-t)(I-tS_n)^{-1}=\frac{1-t}{1-t^n}\sum_{r=0}^{n-1}t^rS_n^r.
\]
The coefficient of \(S_n^r\) in \(T\) is therefore
\[
a_r=\frac{(1-t)t^r}{1-t^n}>0,\qquad 0\le r<n.
\]
Summing \(\sum_{j\ge0}(r+jn+1)t^{r+jn}\) gives the coefficient of \(S_n^r\) in \(T^2\):
\[
b_r=a_r(1-t)\left(r+1+\frac{nt^n}{1-t^n}\right).
\]
It follows that the coefficient of \(S_n^r\) in \(P_n(h)\) is
\[
p_r=a_r\left[(1+\sqrt2)(1-t)\left(r+1+\frac{nt^n}{1-t^n}\right)-\sqrt2\right].\tag{1}
\]
The bracket in (1) is strictly increasing in the integer \(r\); all coefficients are nonnegative **if and only if** \(p_0\ge0\). When \(p_0\ge0\), every \(p_r\) with \(r\ge1\) is strictly positive. Also \(P_n(h)\mathbf1=R(0)\mathbf1=\mathbf1\), so any nonnegative endpoint matrix is stochastic.

**2. One scalar inequality.** The diagonal condition \(p_0\ge0\) from (1) is
\[
(1-t)\left(1+\frac{nt^n}{1-t^n}\right)\ge\frac{\sqrt2}{1+\sqrt2}=\gamma.
\]
Equivalently, with
\[
U_n(t)=\frac{1+(n-1)t^n}{1+t+\cdots+t^{n-1}},
\]
we have \(P_n(h)\ge0\) if and only if \(U_n(t)\ge\gamma\), which is equivalent to \(q_n(t)\ge0\). The denominator \(1+t+\cdots+t^{n-1}\) is strictly positive.

**3. A sharp dimension cut.** For fixed \(0<t<1\), put \(a=-\log t>0\). The formula
\[
U_n(t)=(1-t)\left(1+\frac{n}{e^{na}-1}\right)
\]
is strictly decreasing as a function of real \(n>0\), because the derivative of \(n/(e^{na}-1)\) has numerator \(e^{na}(1-na)-1<0\). Thus it suffices to prove \(U_4(t)>\gamma\) and \(U_5(3/5)<\gamma\).

The elementary rational bounds \(\sqrt2>7/5\) imply \(\beta>2/5\) and \(\gamma<3/5\), whence
\[
5q_4(t)>2-3t-3t^2-3t^3+15t^4=:p(t).
\]
The degree-four Bernstein coefficients of \(p\), after mapping each half interval to \([0,1]\), are respectively
\[
\begin{array}{c|ccccc}
[0,1/2]&2&13/8&9/8&13/32&5/16\\
[1/2,1]&5/16&7/32&3/4&11/4&8
\end{array}
\]
(all strictly positive). Since every Bernstein basis function is nonnegative and their sum is one, \(p(t)>0\) on \([0,1]\); therefore \(q_4(t)>0\), and strict positivity follows for \(2\le n\le4\).

Conversely, direct rational evaluation gives
\[
q_5(3/5)=\frac{7205\sqrt2-10313}{3125}<0,
\]
where the last inequality follows already from \(\sqrt2<10/7\). By monotonicity of \(U_n\), every \(n\ge5\) has \(U_n(3/5)\le U_5(3/5)<\gamma\), hence a genuinely negative diagonal entry at the timestep associated to \(t=3/5\).

**4. Exactly one forbidden interval.** For every \(n\ge2\),
\[
q_n'(t)=-\gamma\sum_{j=1}^{n-1}jt^{j-1}+n(n-1)t^{n-1}.
\]
Its coefficients, arranged by increasing degree, have one sign change. Descartes' rule of signs therefore allows at most one positive root. Since \(q_n'(0)=-\gamma<0\) and \(q_n'(1)=n(n-1)(1-\gamma/2)>0\), there is exactly one critical point in \((0,1)\), which is the strict minimum. Moreover \(q_n(0)=\beta>0\) and \(q_n(1)=n\beta>0\). For \(n\ge5\) the negative value at \(3/5\) forces precisely two simple roots and the claimed sign pattern. The increasing bijection \(h=t/[c(1-t)]\) yields exactly the two positive timestep windows asserted.

**5. Threshold asymptotics.** At each fixed \(t<1\), \(U_n(t)\to1-t\). For \(n\ge5\), the first root moves left as \(n\) increases (by the strict decrease of \(U_n\)), and the second moves right. The limiting first root solves \(1-t=\gamma\), so \(t_n^-\to\beta\) and
\[
\frac{t_n^-}{c(1-t_n^-)}\longrightarrow\frac{\beta}{c\gamma}=1+\sqrt2.
\]
The second root must approach one. Write \(t=e^{-s/n}\). For fixed \(s>0\),
\[
U_n(e^{-s/n})\longrightarrow \frac{s}{e^s-1}.
\]
The right-hand side is strictly decreasing from one to zero, hence has exactly one positive solution \(s_*\) to the level \(\gamma\). Comparing the signs at fixed \(s\) on either side of \(s_*\) brackets the upper root and shows \(-n\log t_n^+\to s_*\). Consequently \(n(1-t_n^+)\to s_*\) and \(h_n^+/n\to1/(cs_*)\).

## Verification

The included `verify.py` uses only the Python 3 standard library. Run `python3 verify.py` in the directory containing the extracted file. It passed 8,541 assertions in the packaged environment. These include exact arithmetic in \(\mathbb Q(\sqrt2)\), exact Bernstein coefficients on both halves of \([0,1]\), the five-state negative witness, full endpoint matrices computed using independent finite-dimensional matrix inversions, and numerical brackets for the two transition roots for several dimensions. The infinite-dimensional family and uniqueness-of-interval assertion are established by the analytic argument above, not by testing a finite number of cases.

The generator orientation is explicit: with \((S_n)_{i,j}=1\) for \(j=i+1\pmod n\), the coefficient \(p_r\) is the entry \((P_n)_{i,i+r}\). Reversing all arrows permutes the coefficients and leaves their signs unchanged. The first public posting date of the focal method analysis is the date of arXiv version 1510.04303v1, not a journal revision date.

## Relationship to prior work

Bonaventura and Della Rocca (2015), Section 3 and equation (3.2), give the underlying TR-BDF2 stability function and the absolute-monotonicity radius \(1+\sqrt2\). Their result provides a universal sufficient forward positivity bound for suitable problems; it does not give a necessary-and-sufficient time-step region for each directed-cycle size. In fact, the present first unsafe threshold strictly exceeds that radius for each finite \(n\ge5\), and positivity eventually recovers at large \(h\).

Zappavigna, Colaneri, Kirkland and Shorten (2012), especially Section 4 and Example 3, study loss of positivity for diagonal Padé discretizations of positive systems and include cyclic-chain and nilpotent-shift structures. Their analyzed rational functions differ from L-stable TR-BDF2; their counterexamples and sufficient conditions do not give the present five-state cutoff, the diagonal-only criterion, or the two exact TR-BDF2 positivity windows. Earlier work on Crank–Nicolson, Radau IIA and two-stage SSP-SDIRK has different stability functions, so its transition formulas do not imply this one by a change of names or graph parameters.

## Limitations

This is a complete statement **only** for common-rate directed cycles and the standard L-stable TR-BDF2 endpoint. It neither establishes unconditional positivity for all Markov generators of at most four states nor rules out other failure modes for non-cyclic generators or unequal rates. It does not assess intermediate stage values, which may differ in sign from endpoints. The root formulas for arbitrary \(n\) are implicit algebraic definitions, not elementary radicals. The supplementary verifier uses finite tests and cannot independently certify the quantified analytic proof. Specialized earlier literature may contain equivalent cyclic-kernel calculations; originality is conditional on the described comparisons and has not received independent external review.

## References

- Luca Bonaventura and Alessandro Della Rocca, *Monotonicity, positivity and strong stability of the TR-BDF2 method and of its SSP extensions*, arXiv:1510.04303v1, first posted 2015-10-14, especially Section 3 and equation (3.2). https://arxiv.org/abs/1510.04303
- Annalisa Zappavigna, Patrizio Colaneri, Stephen Kirkland and Robert N. Shorten, *Essentially Negative News About Positive Systems*, 2012 preprint, Section 4 and Example 3, freely available from the Maynooth University Research Archive. https://mural.maynoothuniversity.ie/id/eprint/3761/
