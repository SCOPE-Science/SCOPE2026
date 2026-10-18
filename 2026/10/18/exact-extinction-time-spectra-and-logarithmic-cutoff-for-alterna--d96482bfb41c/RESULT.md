# Exact extinction-time spectra and logarithmic cutoff for alternating rough approximations of two-matchings

## Finding

Let \(X\) be a finite, nonempty set, and let \(E,F\) be equivalence relations whose classes all have size two. The union of the \(E\)-pairs and \(F\)-pairs is a disjoint union of alternating even cycles, including doubled edges when the two partitions agree on a pair. Suppose these components contain \(2n_1,\ldots,2n_c\) points, with \(n_i\ge1\).

For any subset \(S\subseteq X\), the lower approximation \(L_E(S)\) is the union of the \(E\)-classes entirely contained in \(S\), and likewise for \(L_F\). Define \(S_0=S\) and, for integers \(t\ge1\),
\[
S_t=\begin{cases}L_E(S_{t-1}),&t\text{ odd},\\L_F(S_{t-1}),&t\text{ even} .\end{cases}
\]
Set \(\tau(S)=\min\{t\ge1:S_t=\varnothing\}\) if this set is nonempty, and \(\tau(S)=\infty\) otherwise. Choose \(S\) uniformly among all \(2^{|X|}\) subsets. Define the exact integer
\[
A(n,t)=4^n-1+\sum_{r=1}^{\lfloor n/(t+1)\rfloor}(-1)^r\frac nr\binom{n-rt-1}{r-1}3^r4^{n-r(t+1)},\qquad n,t\ge1.
\]
The sum is empty when \(t\ge n\). **For every positive integer \(t\),**
\[
\boxed{\Pr(\tau\le t)=\prod_{i=1}^c \frac{A(n_i,t)}{4^{n_i}},\qquad
\Pr(\tau=\infty)=1-\prod_{i=1}^c(1-4^{-n_i}).}
\]
In particular, for one connected cycle of length \(2n\), the largest *finite* value of \(\tau\) is exactly \(n\), and all non-full inputs go extinct. Yet for \(n=4^m\), with each fixed integer \(j\),
\[
\boxed{\lim_{m\to\infty}\Pr(\tau\le m+j)
=\exp\!\left(-\tfrac34\,4^{-j}\right).}
\]
The limiting distribution is a nondegenerate **lattice** cutoff with bounded fluctuations around \(\log_4 n\); it is not a continuous Gumbel law. For arbitrary \(n\to\infty\), if \(\{\log_4n\}\to\theta\in[0,1]\), then at integer times \(t=\lfloor\log_4n\rfloor+j\) the limit is \(\exp(-\tfrac34 4^{\theta-j})\). Thus the logarithmically centered distribution has a phase dependence, not a single universal limit over all \(n\).

## Assumptions and scope

The equivalence classes are **exactly pairs**; neither singleton blocks nor blocks of larger size are allowed. The two equivalences may agree on some pairs. All components are finite. A repeated application means one lower approximation per time step, in the fixed order \(E,F,E,F,\ldots\). The initial subset is uniformly random, so its point-membership bits are independent fair Bernoulli variables. The formula for finite \(\tau\) is unconditional, retaining the possibility of a permanent nonempty set. Nothing in this statement concerns upper approximations, arbitrary equivalence classes, or random choices of the partitions themselves.

## Proof

**1. Alternating-cycle coordinates.** In one component of \(2n\) points, label the points \(u_i,v_i\), with indices modulo \(n\), so that the \(E\)-pairs are \(e_i=\{u_i,v_i\}\) and the \(F\)-pairs are \(f_i=\{v_i,u_{i+1}\}\). The case \(n=1\), where the two pairs agree, uses the same convention. Put \(B_i=1\) when \(e_i\subseteq S_0\), and \(B_i=0\) otherwise.

**2. Exact trajectory, including phase.** Induction on \(t\) gives two identities. At odd time \(t=2h+1\), the pair \(e_i\) occurs in \(S_t\) exactly when
\[
\bigwedge_{j=-h}^{h}B_{i+j}=1.
\]
At even time \(t=2h\), the pair \(f_i\) occurs exactly when
\[
\bigwedge_{j=1-h}^{h}B_{i+j}=1.
\]
For \(t=1\) the first identity is the definition of the lower approximation. To pass from an \(E\)-output to an \(F\)-output, an \(F\)-pair must have both its points present; they belong to the adjacent \(E\)-pairs \(e_i\) and \(e_{i+1}\), so the two corresponding Boolean conditions are conjoined. The reverse passage uses \(f_{i-1}\) and \(f_i\). This extends the consecutive window by one pair at every step, proving both formulas for all \(t\), including those greater than \(n\).

Therefore \(S_t=\varnothing\) in a component if and only if the cyclic binary word \(B\) has no run of \(t\) consecutive ones. If \(B\) is identically one, the component stays full forever. Otherwise, the longest cyclic run has length at most \(n-1\), and its extinction time is one more than that length, with extinction time one when all \(B_i=0\). In particular, a component that is not initially full vanishes by time \(n\), and the largest finite extinction time is achieved by a word with one zero and \(n-1\) ones.

**3. Exact cyclic-run enumeration.** Each pair \(e_i\) has four possible point-membership states. Exactly one of these states produces \(B_i=1\); the other three produce \(B_i=0\). Hence there are \(4^n\) equally weighted inputs for a component and the \(B_i\) are independent, each with success probability \(1/4\).

Fix \(n,t\ge1\). Mark position \(i\) when \(B_{i-1}=0\) and \(B_i=B_{i+1}=\cdots=B_{i+t-1}=1\), cyclically. A word other than the all-ones word has a run of \(t\) ones if and only if at least one mark occurs. Two distinct marks can coexist only if their cyclic start positions have separation at least \(t+1\) in each cyclic gap. For \(r\ge1\), the number of unordered configurations of \(r\) such start positions is
\[
C_{n,t,r}=\frac nr\binom{n-rt-1}{r-1},
\qquad 1\le r\le\left\lfloor\frac{n}{t+1}\right\rfloor.
\]
Indeed, distinguish one of the \(r\) starts (\(n\) choices), distribute the remaining distances as a composition of \(n\) into \(r\) cyclic gaps each at least \(t+1\), and divide by the number \(r\) of distinguished starts in one configuration. Requiring those \(r\) marks fixes \(r\) distinct zeros and \(rt\) distinct ones among the \(B_i\); in terms of original two-point states this leaves exactly
\[
3^r4^{n-r(t+1)}
\]
possible inputs. Inclusion–exclusion shows that the number of inputs with **no** marked position is the sum of these contributions, beginning with \(4^n\). The all-ones input has no mark but does have a run of any positive length, so exactly one input must be subtracted. The resulting number is \(A(n,t)\). This also proves the formula for \(n=1\) and \(t\ge n\), where the sum is empty.

**4. Disconnected matchings.** Different cycle components involve disjoint point sets and independently assigned membership bits. The alternating operators act componentwise. Global extinction by time \(t\) is the intersection of the componentwise extinction events, yielding the product formula. A component survives indefinitely precisely when its entire vertex set is in the initial subset, with probability \(4^{-n_i}\). Therefore no component survives indefinitely with probability \(\prod_i(1-4^{-n_i})\), proving the second formula.

**5. Sharp logarithmic cutoff.** On one connected \(2n\)-cycle let \(R_{n,t}\) count the marked starts of \(t\) consecutive full \(E\)-pairs following a non-full pair. Each marker occurs with probability \(a_t=(3/4)4^{-t}\). For fixed positive integer \(r\), compatible ordered \(r\)-tuples of marks are precisely those separated by at least \(t+1\) cyclic positions, and their joint probability is \(a_t^r\); incompatible tuples have joint probability zero. If \(t=\lfloor\log_4n\rfloor+j\), then \(t=O(\log n)\), and the number of compatible ordered \(r\)-tuples is \(n^r(1+O_r(t/n))\). Thus
\[
\mathbb E[(R_{n,t})_r]
= (na_t)^r(1+O_r(t/n)),
\]
where \((\cdot)_r\) denotes the falling factorial. Along any subsequence for which \(\{\log_4n\}\to\theta\), these factorial moments converge to those of a Poisson variable with mean \((3/4)4^{\theta-j}\). The standard factorial-moment characterization of the Poisson distribution therefore gives \(\Pr(R_{n,t}=0)\to\exp(-(3/4)4^{\theta-j})\). Finally, the all-ones word contributes the vanishing discrepancy \(4^{-n}\) between \(R_{n,t}=0\) and extinction by time \(t\). This proves the asserted phase-dependent lattice limit. Taking \(n=4^m\) gives \(\theta=0\) exactly. The tight logarithmic cutoff follows from these limiting distribution functions and their limits as \(j\to\pm\infty\).

## Verification

A standalone standard-library Python program, `verify.py`, independently constructs the two matchings and evaluates each lower approximation directly for every subset on a connected component with \(1\le n\le8\). It compares all predicted final pairs, first-extinction counts, and the exact inclusion–exclusion formula; it also tests seven explicitly disconnected matching systems and independently enumerates four-symbol cyclic words for \(1\le n\le7\).

Running `python verify.py` produced:

`VERIFY_OK connected_subsets=87380 step_window_checks=669924 disconnected_subsets=6736 independent_run_counts=28 n_up_to=8`

These are finite cross-checks of the algebra and counting, **not** a replacement for the all-parameter argument or the Poisson limit proof.

## Relationship to prior work

The study of compositions of lower and upper rough approximations for two equivalence relations is established; notably, Gopaulsingh's *Double Successive Rough Set Approximations* (arXiv:1612.03814, publicly posted December 5, 2016) investigates decomposition and reconstruction of the two-step operators. The source's introduction, definitions, main decomposition and uniqueness theorems, and conclusion discuss reconstructing operators, not the distribution of the extinction time of repeatedly alternating pair-partition approximations. The general longest-head-run paradigm is also classical; neither the Bernoulli-run asymptotics nor inclusion–exclusion as a technique is asserted to be new.

The asserted contribution here is the **exact trajectory identification** for arbitrary pairs of perfect matchings, the resulting product law for the entire finite extinction-time distribution, the distinction between persistent and vanishing components, and its precise phase-dependent stochastic cutoff on a connected cycle. General common-knowledge reachability and worst-case stabilization bounds alone do not specify this distribution under random initial subsets. Publication priority is not independently established, and earlier equivalent statements under epistemic-logic or morphological-erosion terminology remain a possibility.

## Limitations

The result does not address unequal block sizes, upper approximations, nonuniform initial data, or simultaneously random partitions. If the overlap graph has multiple cycles, a proper initial subset can contain a complete component and therefore never go globally extinct; the logarithmic limit theorem is stated for a single growing cycle only. The centered limiting law is lattice-dependent; there is no claim of a continuous weak limit after mere subtraction of \(\log_4n\). No claim is made that known longest-run theory is independently original or that finite computations certify an infinite statement. Independent external assessment of originality and correctness has not been performed.

## References

1. Alexa Gopaulsingh, *Double Successive Rough Set Approximations*, arXiv:1612.03814, version 1 publicly posted 2016-12-05; https://arxiv.org/abs/1612.03814.
2. Chen-Xu Hao and Ting Ma, *Limiting behaviors for longest consecutive switches in an IID Bernoulli sequence*, arXiv:2009.08678, publicly posted 2020-09-18; contextual background on discrete run phenomena, not a claim of direct coverage.
