# Re-entrant positivity of Richardson-extrapolated backward Euler on five-state pure-birth chains
## Finding
Consider the homogeneous unit-rate absorbing pure-birth chain on \(N\) states, with row generator \(Q_N\) defined by \((Q_N)_{ii}=-1\), \((Q_N)_{i,i+1}=1\) for \(1\le i<N\), and a zero final row. One backward-Euler step of length \(h\) is \((I-hQ_N)^{-1}\), and two half-steps are \((I-\tfrac h2Q_N)^{-2}\). The second-order Richardson extrapolate is
\[
E_N(h)=2\left(I-\frac h2Q_N\right)^{-2}-(I-hQ_N)^{-1}.
\]
Every row of \(E_N(h)\) sums to one for every \(h\ge0\). For \(N=2,3,4\), it is entrywise nonnegative exactly when
\[
0\le h\le 2+2\sqrt2.
\]
For \(N=5\), it is entrywise nonnegative exactly when
\[
h=0\qquad\text{or}\qquad \eta\le h\le2+2\sqrt2,
\]
where \(\eta\) is the unique positive root of
\[
p(h)=h^5+18h^4+52h^3+48h^2+2h-12.
\]
Moreover,
\[
0.3959<\eta<0.3960.
\]
Thus the five-state chain has a re-entrant positivity window: every sufficiently small positive step is nonpositive as a Markov transition approximation, positivity returns at \(h=\eta\), and it is lost again only when the transient diagonal changes sign at \(h=2+2\sqrt2\). Five states are the first in this homogeneous pure-birth hierarchy to exhibit the small-step positivity hole.

## Assumptions and scope
The statement is for the homogeneous unit-rate absorbing pure-birth generator above and for the one-step Richardson combination formed from one full backward-Euler step and two half backward-Euler steps. Rate \(\lambda>0\) is recovered by replacing \(h\) with \(\lambda h\). The result does not assert a minimal state dimension over all continuous-time Markov generators or over nonuniform pure-birth chains, and it does not address higher Richardson levels.

## Proof
For scalar decay, define
\[
r(z)=\frac{2}{(1+z/2)^2}-\frac1{1+z}
=\frac{-z^2+4z+4}{(z+1)(z+2)^2}.
\]
On the transient block of the pure-birth chain, \(-Q=I-S\), where \(S\) is the nilpotent one-step upper shift. Functional calculus therefore gives
\[
r\bigl(h(I-S)\bigr)=\sum_{k\ge0} a_k(h)S^k,
\qquad
a_k(h)=\frac{(-h)^k}{k!}r^{(k)}(h).
\]
For the distances needed through five states,
\[
a_0(h)=\frac{-h^2+4h+4}{(h+1)(h+2)^2},
\]
\[
a_1(h)=\frac{-h(h^3-10h^2-20h-8)}{(h+1)^2(h+2)^3},
\]
\[
a_2(h)=\frac{-h^2(h^4-16h^3-48h^2-40h-8)}{(h+1)^3(h+2)^4},
\]
\[
a_3(h)=\frac{-h^4(h^4-22h^3-88h^2-112h-48)}{(h+1)^4(h+2)^5}.
\]
The diagonal coefficient \(a_0\) is nonnegative exactly for \(0\le h\le U\), with
\[
U=2+2\sqrt2.
\]
Each polynomial inside the minus sign in \(a_1,a_2,a_3\) has exactly one positive root by Descartes' rule. Evaluating at \(U\) gives respectively
\[
-16(7+5\sqrt2),\qquad -8(161+114\sqrt2),\qquad -16(143+101\sqrt2),
\]
so their positive roots all lie strictly above \(U\). Hence \(a_1,a_2,a_3>0\) on \(0<h\le U\).

The absorbing-column entry in a row with \(m\) transient states remaining is one minus the sum of the available transient coefficients. For chain sizes \(N=2,3,4,5\), the first-row absorbing entries reduce to
\[
\frac{h(h^2+6h+4)}{(h+1)(h+2)^2},
\]
\[
\frac{h^2(h^3+10h^2+14h+4)}{(h+1)^2(h+2)^3},
\]
\[
\frac{h^4(h^3+14h^2+30h+18)}{(h+1)^3(h+2)^4},
\]
and
\[
\frac{h^4p(h)}{(h+1)^4(h+2)^5},
\]
respectively. The first three are positive for every \(h>0\). In the five-state case, \(p\) has coefficient signs \(+,+,+,+,+,-\), so Descartes' rule gives exactly one positive root \(\eta\). Direct exact evaluation gives \(p(3959/10000)<0<p(99/250)\), proving \(0.3959<\eta<0.3960\). Therefore the only sign obstruction below \(U\) for \(N=5\) is the first-row absorbing entry, which is negative precisely on \(0<h<\eta\). For \(h>U\), \(a_0<0\), so positivity fails for every \(N\ge2\). This proves all stated if-and-only-if ranges.

## Verification
The accompanying `verify.py` uses exact rational arithmetic. It reconstructs the backward-Euler Richardson matrix at \(N=5\) for selected rational steps, checks row sums, checks the exact negative witness below \(\eta\), and verifies the rational root bracket. At \(h=1/4\), the first row is
\[
\left(\frac{316}{405},\frac{3484}{18225},\frac{7252}{273375},\frac{83804}{36905625},-\frac{7799}{36905625}\right),
\]
so the transition approximation has a negative absorbing-state entry despite both backward-Euler constituents being nonnegative. At \(h=1\), every entry is nonnegative. The universal theorem itself is proved algebraically above; these finite checks are corroboration, not a substitute for the proof.

## Relationship to prior work
Fornberg, Zuev, and Lee study Richardson time extrapolation of stable integrators and explicitly frame the question of which stability properties survive extrapolation; their preprint is dated 21 November 2005 and lists MSC 65L06 first. Constantinescu and Sandu give the standard extrapolation construction from repeated smaller steps and explicitly discuss Euler and linearly implicit Euler base methods. Bonaventura and Della Rocca review positivity and monotonicity through absolute monotonicity and emphasize the unconditional monotonicity of implicit Euler. These sources motivate the natural question of what positivity survives a higher-order extrapolation of backward Euler, but the inspected material does not state the exact pure-birth positivity windows proved here.

The closest published semantic-database records found during the literature comparison concern a fourth-order \([2/2]\) Padé map on pure-birth chains and a backward-Euler-filtered Crank-Nicolson lattice step. Those methods use different rational maps and their statements do not imply the present five-state Richardson-backward-Euler classification. A previously recorded result for classical RK4 on the same homogeneous pure-birth family was also checked for overlap; it concerns a polynomial stability function and a different positivity frontier, so neither statement implies the other.

## Limitations
The classification is deliberately narrow: homogeneous pure-birth chains through five states and one second-order Richardson level. It does not establish what happens for arbitrary generators, nonuniform rates, or larger state counts. The originality comparison found no implication-equivalent statement in the inspected sources or published semantic index, but older SSP or extrapolation literature could express related derivative conditions under different terminology.

## References
1. B. Fornberg, J. Zuev, J. Lee, *Stability and accuracy of time-extrapolated ADI-FDTD methods for solving wave equations*, preprint submitted 21 November 2005; later J. Comput. Appl. Math. 200 (2007), 178–192. https://www.colorado.edu/amath/sites/default/files/attached-files/extrap03.pdf
2. E. M. Constantinescu, A. Sandu, *Achieving Very High Order for Implicit Explicit Time Stepping: Extrapolation Methods*, ANL/MCS-TM-306, April 2009. https://www.mcs.anl.gov/uploads/cels/papers/TM-306.pdf
3. L. Bonaventura, A. Della Rocca, *Monotonicity, positivity and strong stability of the TR-BDF2 method and of its SSP extensions*, arXiv:1510.04303, 14 October 2015. https://arxiv.org/abs/1510.04303
