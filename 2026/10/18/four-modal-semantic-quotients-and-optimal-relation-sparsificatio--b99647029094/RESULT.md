# Four-modal semantic quotients and optimal relation sparsification on finite intuitionistic chains

## Finding

Let \(W_n=\{0<1<\cdots<n-1\}\) with \(n\ge1\), and let \(R\subseteq W_n^2\) be arbitrary. There is a complete, explicitly testable, rowwise characterization of the pointwise semantic equivalence classes of \(R\) in the *full* four-modal intuitionistic Heyting--Brouwer language. Each class has a representative containing at most two arrows from any world; the exact class-minimum number of arrows follows from independent rowwise tests. The universal worst-case minimum is \(1\) for \(n=1\) and \(2n\) for \(n\ge2\), both attained. The numbers of semantic classes for \(n=1,2,3,4,5\) are exactly \(2,16,279,7171,235152\).

## Assumptions and scope

A valuation assigns each propositional letter an upward-closed subset of the fixed finite chain. The full language includes the Heyting and dual-Heyting implications, \(\wedge,\vee,\top,\bot\), and all four modal operators of Balbiani and Gencer [1]. Their precise clauses for any upward-closed truth set \(U\) are

\[
\begin{aligned}
\mathsf P_R(U)&=\{s:\exists i\le s\ \exists u\ (iRu\land u\in U)\},\\
\mathsf Q_R(U)&=\{s:\forall i\ge s\ \exists u\ (iRu\land u\in U)\},\\
\mathsf E_R(U)&=\{s:\exists i\le s\ \forall u\ (iRu\Rightarrow u\in U)\},\\
\mathsf D_R(U)&=\{s:\forall i\ge s\ \forall u\ (iRu\Rightarrow u\in U)\}.
\end{aligned}
\]

These are, respectively, the Přenosil diamond, Wijesekera diamond, dual necessity, and ordinary necessity. We use distinct symbols only to disambiguate the operators in the four-profile theorem. This problem concerns pointwise agreement for the *same* valuation on a fixed ordered carrier, a stronger relation than merely having the same globally valid formulas.

Write \(R[i]=\{u:iRu\}\). Let

\[
 h_i=\begin{cases}-1&R[i]=\varnothing\\\max R[i]&R[i]\ne\varnothing\end{cases},\qquad
 \ell_i=\begin{cases}n&R[i]=\varnothing\\\min R[i]&R[i]\ne\varnothing.\end{cases}
\]

Define the signature, using the exact index ranges,

\[
 P_i=\max_{0\le j\le i}h_j,\qquad Q_i=\min_{i\le j<n}h_j,\qquad
 E_i=\max_{0\le j\le i}\ell_j,\qquad D_i=\min_{i\le j<n}\ell_j.
\]

All four sequences are nondecreasing. For \(i\in W_n\), define sets of permissible row maxima and minima

\[
\begin{aligned}
 H_i=\{h\in\{-1,\ldots,n-1\}:&\ Q_i\le h\le P_i,\\
 & (i=0\text{ or }P_i>P_{i-1})\Rightarrow h=P_i,\\
 & (i=n-1\text{ or }Q_i<Q_{i+1})\Rightarrow h=Q_i\},\\
 L_i=\{\ell\in\{0,\ldots,n\}:&\ D_i\le\ell\le E_i,\\
 & (i=0\text{ or }E_i>E_{i-1})\Rightarrow\ell=E_i,\\
 & (i=n-1\text{ or }D_i<D_{i+1})\Rightarrow\ell=D_i\}.
\end{aligned}
\]

Here a comparison to the nonexistent previous or next entry is *not evaluated* when the corresponding boundary disjunct is true. Define

\[
 T_i=\{(\ell,h)\in L_i\times H_i:(\ell,h)=(n,-1)\ \text{or}\ 0\le\ell\le h<n\}.
\]

The class of profile quadruples is exactly the set of nondecreasing bounded quadruples with \(T_i\ne\varnothing\) for all \(i\). For each row let \(c_i\) be the least value of the cost function

\[
 c(\ell,h)=\begin{cases}0&(\ell,h)=(n,-1),\\1&0\le\ell=h<n,\\2&0\le\ell<h<n.\end{cases}
\]

among \(T_i\). The minimum number of arrows in the corresponding semantic equivalence class is \(\sum_{i=0}^{n-1}c_i\).

## Proof

**1. Exact action on upsets and necessity of the signature.** Every upset is uniquely \(U_j=\{j,j+1,\ldots,n-1\}\) for \(0\le j\le n\), including \(U_n=\varnothing\). A row meets \(U_j\) precisely if \(h_i\ge j\), and a row is contained in \(U_j\) precisely if \(\ell_i\ge j\), with the empty-row conventions taking care of both vacuity and nonexistence. Direct substitution into the four semantic clauses yields, for every \(s,j\),

\[
 s\in\mathsf P_R(U_j)\iff P_s\ge j,\quad
 s\in\mathsf Q_R(U_j)\iff Q_s\ge j,\quad
 s\in\mathsf E_R(U_j)\iff E_s\ge j,\quad
 s\in\mathsf D_R(U_j)\iff D_s\ge j.
\]

Thus equality of the four profiles gives equality of each modal operator on the entire upset algebra. It follows by induction on formulas, because all propositional connectives (including both implications) depend only on the order and the input truth sets, that the full nested language has identical pointwise truth. Conversely, assigning a single variable \(p\) the value \(U_j\), and observing each of the four one-modal formulas, recovers every comparison of every profile entry with every \(j\). As profile entries lie in the stated finite integer ranges, identical one-modal formula truth forces equal profiles. This also proves that nesting introduces no hidden additional invariant.

**2. Local realizability is sufficient and necessary.** If row extrema are given, the inequalities defining \(H_i\) hold because a prefix maximum bounds its final summand from above and a suffix minimum bounds its initial summand from below. Whenever the prefix maximum strictly increases, its new final summand must equal the new prefix maximum, and the initial boundary row does too. Whenever a suffix minimum strictly increases on moving right, the removed initial summand must equal its old minimum, and the final boundary row does too. The same reasoning applies to row minima and the sequences \(E,D\). Therefore every realized profile gives nonempty \(T_i\).

Conversely assume each \(T_i\) is nonempty and choose any pair \((\ell_i,h_i)\in T_i\) independently. For each \(i\), choose \(R[i]=\varnothing\) when \((\ell_i,h_i)=(n,-1)\), otherwise \(R[i]=\{\ell_i,h_i\}\). The imposed bounds and boundary/strict-jump equalities reconstruct \(P\) and \(E\) from left to right by induction: if the desired prefix maximum changes, the new row supplies it, and otherwise no row exceeds it. The same argument reconstructs \(Q\) and \(D\) from right to left. Hence the prescribed quadruple is exactly the resulting signature, proving sufficiency and independent row choices.

**3. Exact minimal arrows and global optimum.** A row realizing the empty sentinel needs no arrow; a nonempty row with equal minimum and maximum needs exactly one; and a row with distinct minimum and maximum necessarily contains both extreme values and needs at least two arrows. In each case the construction in Step 2 attains that lower bound. Since row choices are independent, minimizing each row separately gives exactly \(\sum_i c_i\). This proves the universal \(2n\) upper bound. For \(n\ge2\), take \(R[i]=\{0,n-1\}\) at every row. In its signature \(Q_0=n-1\) forces *every* row maximum to be \(n-1\), while \(E_{n-1}=0\) forces *every* row minimum to be \(0\). Each equivalent row needs two arrows, proving the lower bound \(2n\). At \(n=1\), the empty and singleton relations are distinguishable and a single arrow is necessary in the nonempty class.

**4. Exact finite class census.** Enumerate all \(1+n(n+1)/2\) possible row-extrema pairs (the sentinel plus \(0\le\ell\le h<n\)), form all \(n\)-fold products, and compute their signatures. Step 2 proves this traverses every class, and Step 1 proves equality of signatures is *exactly* class identity. This finite exhaustive procedure yields \(2,16,279,7171,235152\) distinct signatures for \(n=1,2,3,4,5\), respectively. The included standalone verifier reproduces the counts and, separately for \(n\le4\), checks every one of the \(2^{n^2}\) raw relations against the direct modal semantics. This finite computation is not used to prove the general theorem.

## Verification

Run `python3 verify.py` with Python 3 and the standard library. Expected final line: `VERIFY_OK`. For carrier sizes up to four the script computes the four modal truth tables from their quantifier definitions for every raw relation and every upset, compares these with the claimed profiles, and checks class-optimal edge minima against an independent extremal-row enumeration. For sizes up to three it independently enumerates all monotone candidate signatures and tests the local realizability criterion and optimal row costs. For size five it exhaustively enumerates all \((1+n(n+1)/2)^n\) extremal-row combinations; it does *not* enumerate all \(2^{25}\) raw relations. A run produces the class counts above and maximal class-minima \(1,4,6,8,10\) arrows for \(n=1,\ldots,5\). General claims rest on the four proof steps, not on finite extrapolation.

## Relationship to prior work

Balbiani and Gencer [1] introduce exactly these four modal truth clauses for arbitrary preorders and arbitrary accessibility relations, and establish results on eliminability, frame definability, axiomatization, and decidability. Their Propositions 20–24 and 73–78 have a different conclusion from a *complete finite-chain pointwise relation quotient* with a rowwise realizability test and exact least-arrow representative. The new assertion concerns no additional confluence assumption; consequently it does not claim to strengthen axiomatization or decidability in [1].

Fernández-Duque [2] studies Fine selection and the finite model property for Fischer Servi-style IK4 on birelational frames. A filtration or finite model property for one logic is not the same statement as equality of the four named truth transformers on all upsets of a fixed chain, nor does it provide the exact class-minimum number of arrows. Prior work [3,4] develops intuitionistic modal semantics and modal filtration but is not used as a proof of the quotient criterion.

## Limitations

The theorem is restricted to *finite linearly ordered* persistent Kripke carriers, with arbitrary accessibility and these exact four semantic clauses. It is not a criterion for partial orders, nonpersistent valuations, alternative modalities, bisimulation between varying carriers, or equality of mere sets of globally valid formulas. The worst-case \(2n\) sparse-representative guarantee does not extend to infinite chains: one row with infinitely many increasingly large successors may be needed to preserve all tests by nonempty upset tails. The exact class-count values were computed only through five worlds; the characterization remains valid for every positive finite size and should not be confused with a closed-form expression for arbitrary size. An undiscovered equivalent result in older modal-algebra terminology remains an originality risk.

## References

[1] P. Balbiani and Ç. Gencer, *Four intuitionistic modal connectives*, arXiv:2606.07348v1, first posted 2026-06-05. Sections 3–5 and 11–12; especially modal semantic clauses, Propositions 20–24 and 73–78. https://arxiv.org/abs/2606.07348

[2] D. Fernández-Duque, *Fine Selection for Intuitionistic Modal Logic*, arXiv:2609.27078v2, posted 2026-09-29. https://arxiv.org/abs/2609.27078

[3] A. Simpson, *The Proof Theory and Semantics of Intuitionistic Modal Logic*, University of Edinburgh doctoral thesis, 1994.

[4] M. Takano, *Finite Model Property for an Intuitionistic Modal Logic*, Nihonkai Mathematical Journal **14** (2003), 125–132.
