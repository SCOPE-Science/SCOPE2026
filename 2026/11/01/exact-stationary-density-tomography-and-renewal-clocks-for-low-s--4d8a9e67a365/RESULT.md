# Exact stationary-density tomography and renewal clocks for low-slope random interval maps

## Finding

For independent random iteration of the maps
\[
T_b(x)=\begin{cases}2x,&0\leq x\leq\tfrac12,\\2^{-b}(2x-1),&\tfrac12<x\leq1,\end{cases}\qquad b\in\{1,2,\ldots\},
\]
with arbitrary strictly positive probabilities on a nonempty subset of positive integers (and zero probabilities permitted elsewhere), let \(p_b=\Pr(B=b)\). Put \(Y=(1/2,1]\) and \(J_m=(2^{-m-1},2^{-m}]\), \(m\geq1\).

An absolutely continuous, Lebesgue-equivalent, conservative ergodic invariant measure has the **exact density**, up to a constant \(c>0\),
\[
h(x)=\begin{cases}c,&x\in Y,\\c\sum_{b\geq1}p_b2^{\min(b,m)},&x\in J_m,\ m\geq1.\end{cases}
\]
Its total mass is \(c(\mathbb EB+2)/2\). Hence an equivalent stationary **probability** exists precisely when \(\mathbb EB<\infty\), in which case \(c=2/(\mathbb EB+2)\); otherwise the equivalent invariant measure is infinite but sigma-finite.

Write \(h_0=c\) and \(h_m=h|_{J_m}\). The complete switching law is **identifiable from the stationary one-time density**:
\[
\Pr(B\geq m)=\frac{h_m-h_{m-1}}{c2^{m-1}},\qquad
p_m=\frac{h_m-h_{m-1}}{c2^{m-1}}-\frac{h_{m+1}-h_m}{c2^m},\qquad m\geq1.
\]
Conversely, the attainable positive dyadic-step invariant-density profiles (up to scale) are exactly those with \(h_0=c>0\) and the scaled first differences \(q_m=(h_m-h_{m-1})/(c2^{m-1})\) satisfying \(q_1=1\), \(1\geq q_1\geq q_2\geq\cdots\geq0\), and \(q_m\to0\). They are normalizable to probabilities precisely when \(\sum_{m\geq1}q_m<\infty\).

The successive original-time return intervals to \(Y\), when started in the induced invariant probability (normalized Lebesgue measure on \(Y\)), are independent and identically distributed as
\[
R=B+1+G,\qquad \Pr(G=j)=2^{-j-1}\ (j\geq0),\qquad
\mathbb E[z^R]=\frac{z\,\mathbb E[z^B]}{2-z}\quad (0\leq z<1).
\]
Thus \(\mathbb ER=\mathbb EB+2\) (possibly infinite); finite stationary return frequency is \(1/(\mathbb EB+2)\), while for infinite mean the renewal frequency is zero.

## Assumptions and scope

The integer-valued random variables \(B_t\) are independent and identically distributed and independent of the starting point. The map \(T_{B_t}\) is applied at each integer time, with the branch determined by the current state. Boundaries of the dyadic partition and the fixed point at zero have zero mass for the stated absolutely continuous measures. Assertions about uniqueness concern invariant measures equivalent to Lebesgue measure, not arbitrary singular stationary measures (the atom at zero is invariant). A stationary **probability** is considered in the Lebesgue-equivalent class only.

## Proof

**1. Transfer identity.** On \(Y\) the only inverse branch has the form \(x\mapsto x/2\in J_1\), of Jacobian \(1/2\); the right branch never maps into \(Y\). On \(J_m\), the same left preimage contributes \(h_{m+1}/2\). A right-branch preimage exists exactly for \(b\leq m\) and contributes \(p_b 2^{b-1}h_0\). Thus the stationarity equations are
\[
h_0=\tfrac12h_1,\qquad h_m=\tfrac12h_{m+1}+\frac{h_0}{2}\sum_{b\leq m}p_b2^b\quad (m\geq1).
\]
The proposed formula has \(h_1=2c\) and
\[
\frac{h_{m+1}}2+\frac c2\sum_{b\leq m}p_b2^b
=c\sum_{b\leq m}p_b2^b+c2^m\sum_{b>m}p_b=h_m,
\]
so it is invariant pointwise off the dyadic boundaries. Every \(h_m\) is finite and at least \(c\); hence this is a Lebesgue-equivalent sigma-finite measure. The established conservativity/ergodicity of this precise family [1, Proposition 4.1 and Theorem 3.1], together with [1, Remark 3.1(I)], gives uniqueness up to constant in the equivalent invariant class.

**2. Exact mass and the probability threshold.** The length of \(J_m\) equals \(2^{-m-1}\). For every fixed integer \(b\geq1\),
\[
\sum_{m\geq1}2^{-m-1}2^{\min(b,m)}=\frac b2+\frac12.
\]
Tonelli's theorem (valid also for infinite expectations), plus \(|Y|=1/2\), gives
\[
\int_0^1h(x)\,dx=c\left(\frac12+\sum_bp_b\frac{b+1}{2}\right)
=\frac c2(\mathbb EB+2).
\]
No finite equivalent invariant measure exists in the infinite-mean case because the equivalent invariant measure is unique up to scale.

**3. Tomography and converse.** Since \(2^{\min(b,m)}-2^{\min(b,m-1)}\) equals \(2^{m-1}\) exactly if \(b\geq m\) and zero otherwise, the first differences give \(h_m-h_{m-1}=c2^{m-1}\Pr(B\geq m)\). Taking consecutive differences yields \(p_m\) as stated. Conversely, from any admissible sequence \(q_m\), define \(p_m=q_m-q_{m+1}\geq0\). Then \(\sum_mp_m=q_1-\lim_mq_m=1\) and \(\Pr(B\geq m)=q_m\); summing the difference recurrence reconstructs exactly the proposed invariant profile. Finally \(\mathbb EB=\sum_m\Pr(B\geq m)=\sum_mq_m\).

**4. Induced clock.** From \(x\in Y\), after one step the orbit is at \(2^{-B}(2x-1)\), then doubles deterministically until it reaches \(Y\). With \(U=2x-1\), let \(G\) be the number of initial zero binary digits of \(U\). Under normalized Lebesgue measure on \(Y\), \(U\) is uniform, so \(\Pr(G=j)=2^{-j-1}\). The first return occurs at physical time \(B+1+G\); the returned point is \(2^G U\). Conditional on \(G=j\), this returned point is uniform on \(Y\); moreover the next independent random label is independent. The successive dyadic digit blocks defining \(G\) are therefore independent, proving the iid return sequence. Its generating function and mean follow immediately. The finite-case return frequency follows from the strong law or the renewal theorem. When the iid nonnegative return increments have infinite mean, truncation in the strong law proves their sample mean tends to infinity and return frequency tends to zero.

## Verification

The accompanying standalone `verification_checks.py` uses exact `Fraction` arithmetic. Six distinct finite-support switching laws, including degenerate and three-point distributions, passed 1,128 finite identities: transfer balance on 49 dyadic shells, tail inversion, mass normalization, and explicit return-time probabilities. The proof above is the basis for all-countable-law assertions; finite examples do not establish them.

## Relationship to prior work

Inoue and Toyokawa [1, §4.1] introduced this exact family and proved existence of its Lebesgue-equivalent sigma-finite measure and *order-comparable* dyadic shell masses. Their general §3 gives existence, uniqueness up to scale, and asymptotic bounds; it does not state the exact shell-by-shell density, invertible full switching-law parametrization, attainable-profile criterion or iid physical-return-time law above. Inoue [2] provides the broad induced-operator principle for random interval systems; the present explicit equations and inverse characterization are not a restatement of that general construction. Kalle and Maggioni [3] give density formulas under uniform expansion-on-average (condition (A2)); the present family has right-branch averaged inverse slope \(\sum_bp_b2^{b-1}\geq1\), so their hypothesis fails. Boyarsky [4] studies random finite Markov families; individual finite-support specializations may be computable by Markov matrices, whereas the present result treats arbitrary countable laws, including null-recurrent infinite-measure cases and complete one-time identifiability.

## Limitations

All results describe the specified dyadic linear family and annealed invariant measures. They do not assert identification under observation noise, efficient statistical estimation from finite data, or a unique stationary measure among singular measures. The novelty assessment is relative to examined literature; general inducing frameworks could yield these formulas after further specialization. Independent scientific validation and exhaustive publication-priority checking have not been performed.

## References

[1] T. Inoue and H. Toyokawa, *Invariant measures for random piecewise convex maps*, arXiv:2303.10873 (public 2023-03-20), especially Theorem 3.1, Remark 3.1(I), and §4.1, Proposition 4.1. https://arxiv.org/html/2303.10873v1

[2] T. Inoue, *First return maps of random maps and invariant measures*, Nonlinearity 33 (2020), 249–275, online 2019-11-22, DOI 10.1088/1361-6544/ab4c83. https://doi.org/10.1088/1361-6544/ab4c83

[3] C. Kalle and M. Maggioni, *Invariant densities for random systems of the interval*, arXiv:1805.11430 (2018), §2, condition (A2). https://arxiv.org/abs/1805.11430

[4] A. Boyarsky, *Uniqueness of invariant densities for certain random maps of the interval*, Canad. Math. Bull. 30 (1987), 301–308. https://www.academia.edu/121875132/Uniqueness_of_invariant_densities_for_certain_random_maps_of_the_interval
