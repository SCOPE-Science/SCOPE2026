# A sharp increasing-hazard criterion for universally divisible quantum renewal resetting

## Finding

For discrete-time resetting to a fixed quantum state, a nondecreasing reset hazard is **necessary and sufficient for complete-positive divisibility uniformly over every finite-dimensional channel and every reset state**. A strict decrease at any age admits an explicit finite-dimensional cyclic-unitary witness for which the reduced evolution is not even positive-divisible. The result gives a sharp dividing line within genuinely age-dependent, rather than clock-time-dependent, renewal resetting.

## Assumptions and scope

Fix a sequence \(h_n\in(0,1)\), \(n\ge1\), with \(S_n=\prod_{j=1}^n(1-h_j)\to0\) and \(S_0=1\). At each time step the system is reset to a fixed density matrix \(\sigma\) with conditional probability \(h_{a+1}\), where \(a\) is the integer number of steps since the last reset; otherwise a fixed completely positive trace-preserving map \(\mathcal E\) acts and the age increases by one. The initial age is zero and the initial density matrix is unrestricted. The reset event renews the age. All dimensions \(d\ge2\), fixed CPTP maps on \(M_d\), and reset density matrices are admitted.

Let \(\Phi_t\) be the unconditional dynamical map at integer \(t\ge0\). We say that \(\Phi\) is CP-divisible if, for every \(t\ge s\ge0\), there exists a CPTP map \(\Lambda_{t,s}\) with \(\Phi_t=\Lambda_{t,s}\circ\Phi_s\). Replacing CPTP by positive trace-preserving defines P-divisibility.

**Theorem (universal sharpness).** The following assertions are equivalent:

1. \(h_{n+1}\ge h_n\) for all \(n\ge1\).
2. For every \(d\ge2\), every CPTP \(\mathcal E:M_d\to M_d\), and every reset state \(\sigma\), the family \((\Phi_t)_{t\ge0}\) is CP-divisible.
3. For every such triple, the family is P-divisible.

Moreover, if \(h_{m+1}<h_m\) for any \(m\ge1\), condition 3 already fails in dimension \(d=m+2\) with a pure reset and a cyclic unitary update. The criterion concerns the Schrödinger-picture reduced maps, not independently defined Heisenberg-picture intertwining maps.

## Proof

**Renewal decomposition.** Put \(p_j=S_{j-1}h_j\), \(j\ge1\), and let the ordinary renewal mass be \(\nu_0=1\) and
\[
\nu_t=\sum_{j=1}^t\nu_{t-j}p_j\quad(t\ge1).
\]
Thus \(\nu_t\ge0\), \(\nu_1=h_1>0\), and \(\nu_t\) is the probability of a reset at time \(t\). Conditioning on the last reset gives, for every operator \(X\),
\[
\Phi_t(X)=S_t\mathcal E^t(X)+\operatorname{Tr}(X)B_t,
\qquad B_0=0,
\qquad B_t=\sum_{s=1}^t\nu_sS_{t-s}\mathcal E^{t-s}(\sigma).
\]
All \(B_t\) are positive, and \(\operatorname{Tr}B_t=1-S_t\) by the disjoint last-reset partition. This formula also fixes the trace-preserving linear extension of \(\Phi_t\) from states to all operators.

**Explicit intermediate map.** Define
\[
q_t=\frac{S_{t+1}}{S_t}=1-h_{t+1},\qquad Y_t=B_{t+1}-q_t\mathcal E(B_t).
\]
The positive survival probabilities make \(q_t\) well defined. Reindexing the two renewal sums yields the exact identity
\[
\boxed{Y_t=\nu_{t+1}\sigma+
\sum_{s=1}^t\nu_sS_{t-s}
\bigl(h_{t+1}-h_{t+1-s}\bigr)
\mathcal E^{t+1-s}(\sigma).}
\]
From trace preservation and the last-reset partition,
\[
\operatorname{Tr}Y_t=(1-S_{t+1})-q_t(1-S_t)=h_{t+1}.
\]
If \(h_n\) is nondecreasing, every coefficient in the boxed formula is nonnegative, so \(Y_t\ge0\). Set
\[
\Lambda_{t+1,t}(X)=q_t\mathcal E(X)+\operatorname{Tr}(X)Y_t.
\]
This is CPTP: it is the convex combination of \(\mathcal E\) with weight \(q_t\) and the replacement channel \(X\mapsto\operatorname{Tr}(X)Y_t/h_{t+1}\) with weight \(h_{t+1}\). Using the renewal decomposition,
\[
\Lambda_{t+1,t}(\Phi_t(X))
=q_t S_t\mathcal E^{t+1}(X)+\operatorname{Tr}(X)
\bigl(q_t\mathcal E(B_t)+Y_t\bigr)
=\Phi_{t+1}(X).
\]
Composition of the one-step CPTP maps establishes condition 2 at every pair of times. Condition 2 trivially implies condition 3.

**Sharp converse by a cyclic witness.** Suppose there is \(m\ge1\) with \(h_{m+1}<h_m\). Take \(d=m+2\), basis \(\{|0\rangle,\ldots,|m+1\rangle\}\), the cyclic shift \(U|j\rangle=|j+1\bmod d\rangle\), the update \(\mathcal E(X)=UXU^\dagger\), and \(\sigma=|0\rangle\langle0|\). Every \(B_t\) and \(Y_t\) is then diagonal in this basis. In the boxed expression for \(Y_m\), the term with \(s=1\) is the **only** term supported on \(|m\rangle\langle m|\): the term with \(s\ge2\) is supported on site \(m+1-s\le m-1\), and the first term on site zero. Therefore
\[
\langle m|Y_m|m\rangle
=\nu_1S_{m-1}(h_{m+1}-h_m)
=h_1S_{m-1}(h_{m+1}-h_m)<0.
\]
For every \(t\), \(\Phi_t\) is invertible as a **linear map on the full operator space** in this unitary example. Indeed, if \(\Phi_t(X)=0\), trace preservation gives \(\operatorname{Tr}X=0\), and hence \(S_tU^tXU^{-t}=0\), which implies \(X=0\) because \(S_t>0\). Thus any intermediate \(\Lambda_{m+1,m}\) is uniquely forced to equal the displayed \(q_m\mathcal E+\operatorname{Tr}(\cdot)Y_m\). Applied to the positive projector \(|m\rangle\langle m|\), its unitary term lies on site \(m+1\), whereas its site-\(m\) matrix element is the strictly negative number above. The unique intermediate is not positive. Hence condition 3 fails, completing the equivalence.

**Exact small witness.** For \(h_1=2/5\), \(h_2=1/5\), the cyclic shift in dimension three gives \(\nu_2=7/25\), \(Y_1=\operatorname{diag}(7/25,-2/25,0)\), and \(q_1=4/5\). The uniquely determined intermediate sends \(|1\rangle\langle1|\) to a trace-one diagonal operator with eigenvalues \(7/25,-2/25,4/5\), exhibiting nonpositivity by an exact rational certificate. Any continuation of the hazards with a proper waiting-time distribution preserves this witness.

## Verification

The standalone `check.py` constructs the last-reset decomposition and explicit intermediate maps independently. It verifies the renewal-sum identity and channel composition for finite steps using randomly generated finite-dimensional random-unitary channels and reset states, tests positivity of each Choi matrix in nondecreasing-hazard examples, and verifies exact rational negative cyclic witnesses for fifteen drop positions. With Python 3 and NumPy installed, run `python check.py`. The checker outputs 60 passing finite-step groups and 15 exact negative witnesses. These finite tests are checks of implementation and algebra; the dimension-uniform, infinite-time equivalence is proved above, not inferred from sampling.

## Relationship to prior work

Carollo and Wald, arXiv:2601.13367v1, derive the exact renewal map and analyze nondivisibility through numerical and analytic witnesses, treating constant reset hazards as a CP-divisible special case. Their full main text and supplementary derivations do not provide the present necessary-and-sufficient **universal** increasing-hazard criterion or the converse finite-dimensional cyclic construction. This result builds on their renewal decomposition, rather than claiming that decomposition as new.

Megier, Smirne, and Vacchini, arXiv:2007.11276v1, investigate general quantum semi-Markov dynamics, particular dephasing/amplitude-damping structures, and coarse-grained Markovian approximations. Those statements do not assert the exact fixed-reset-state, arbitrary-CPTP, discrete-time universal criterion proved here. Wald et al., arXiv:2410.11497v1, analyze steady states and correlations under discrete-time resetting, rather than this universal characterization of intermediate-map positivity. Earlier results for history-dependent **selection** of past states are also different: they do not have the renewal-to-fixed-state hazard model used here.

## Limitations

The proof assumes a strictly positive hazard smaller than one at every finite age, an independently renewed waiting time after each reset, the **same** CPTP update between resets, and a fixed reset density matrix. Proper waiting times are assumed explicitly. The equivalence is universal over all finite dimensions/channels: for a specified channel and reset state, CP-divisibility can hold even with a decreasing hazard. The result makes no claim of process-tensor Markovianity, equivalence to microscopic memorylessness, or divisibility under an independently defined Heisenberg intertwining convention. Nothing is asserted for negative effective resetting probabilities, hazard values exactly zero or one, time-dependent underlying channels, or reset states conditioned on measurement outcomes.

## References

1. Federico Carollo and Sascha Wald, *Stochastic resetting induces quantum non-Markovianity*, arXiv:2601.13367v1, first posted 19 January 2026, https://arxiv.org/html/2601.13367v1 (including supplementary material).
2. Nina Megier, Andrea Smirne, and Bassano Vacchini, *Evolution equations for quantum semi-Markov dynamics*, arXiv:2007.11276v1, https://arxiv.org/pdf/2007.11276.
3. Sascha Wald, Li Hua Yao, Thierry Platini, Chris Hooley, and Federico Carollo, *Stochastic resetting in discrete-time quantum dynamics: steady states and correlations in few-qubit systems*, arXiv:2410.11497v1, https://arxiv.org/pdf/2410.11497.
