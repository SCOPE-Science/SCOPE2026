# Ternary square-digit happy numbers have no natural density

## Finding
For each positive integer \(n\), define \(S(n)\) to be the sum of the squares of its base-three digits. Let
\[
\mathcal H=\{n\ge 1 : S^{\circ k}(n)=1\text{ for some }k\ge0\},
\qquad
A(X)=|\mathcal H\cap[1,X]|.
\]
Then the upper and lower asymptotic densities satisfy the strict quantitative bounds
\[
\boxed{\limsup_{X\to\infty}\frac{A(X)}{X}>0.3718,
\qquad \liminf_{X\to\infty}\frac{A(X)}{X}<0.11004.}
\]
Thus the natural density of ternary square-digit happy numbers does not exist.

## Assumptions and scope
The result concerns all positive integers, using the ordinary leading-nonzero convention for base-three representations. A number is happy if its squared-digit iteration reaches the fixed point \(1\). The only infinite asymptotic input is Gilmer's published density-transfer theorem [1, Theorem 4.1], applied with base \(b=3\), digit values \((0,1,4)\), digit mean \(\mu=5/3\), variance \(\sigma^2=26/9\), and both the basin of \(1\) and its complement. The two finite starting shells have digit lengths \(136\) and \(224\), respectively.

## Proof
**1. Finite reduction and exact digit counting.** If \(n\) has \(d\ge4\) ternary digits, then \(S(n)\le4d<3^{d-1}\le n\). Hence all trajectories eventually enter \([1,26]\). Directly applying the explicitly defined map within that finite interval gives
\[
\{t\in[1,26]:t\text{ eventually reaches }1\}=\{1,3,9,13,17,23,25\}.
\]
In particular, every sufficiently short trajectory is classified without numerical approximations; the attached verifier checks each of the \(26\) cases and implements a finite orbit classifier for larger intermediate digit sums.

Define the nonnegative integers
\[
 c_{m,t}=[z^t](1+z+z^4)^m,
 \quad c_{0,0}=1,\quad c_{0,t}=0\ (t\ne0).
\]
With negative-index coefficients interpreted as zero, the identity
\[
 c_{m+1,t}=c_{m,t}+c_{m,t-1}+c_{m,t-4}
\]
is an exact recurrence. Write \(h(u)=1\) if iterating \(S\) from \(u\) reaches \(1\), and \(h(u)=0\) otherwise. A ternary integer having exactly \(m\) digits has leading digit \(1\) or \(2\). The remaining \(m-1\) digits contribute the generating polynomial above, so the exact number of happy integers in the shell \([3^{m-1},3^m-1]\) is
\[
H_m=\sum_{t=0}^{4(m-1)}c_{m-1,t}\bigl(h(t+1)+h(t+4)\bigr),
\qquad D_m=2\cdot3^{m-1}.
\]
Both integers can be computed in \(O(m^2)\) additions with no floating-point arithmetic. The attached exact-integer calculation establishes
\[
\begin{aligned}
 H_{136}&=19178055136292655461250264410064170536687778419624961726071277806,\\
 D_{136}&=51570267343028562792232297895818356643676497504614529011190107414,\\
 H_{224}&=5502891093366456208838489170975333617574192427931732105330166845785211283754520497189096844380105418413175,\\
 D_{224}&=50011490507388534231836533093323754201895703848958311366223884536640134575228323641611674117863924169133654.
\end{aligned}
\]
Cross multiplication with integers proves the strict bounds
\[
\frac{H_{136}}{D_{136}}>\frac{37188}{100000},
\qquad \frac{H_{224}}{D_{224}}<\frac{110033}{1000000}.
\]
Small shells of lengths \(2\) through \(7\) are also checked against direct enumeration as an independent validation of the combinatorial recurrence.

**2. Verification of the transfer hypotheses.** Gilmer [1, Definition 3.1] calls an interval \(m\)-strict when it lies inside \([3^{m-1},3^m-1]\) and has exactly \(3^{3m/4}\) consecutive integers. For each \(m\in\{136,224\}\), the entire shell partitions into \(2\cdot3^{m/4-1}\) such consecutive intervals. Consequently one \(136\)-strict interval has happy density at least \(H_{136}/D_{136}\), and one \(224\)-strict interval has *nonhappy* density at least \(1-H_{224}/D_{224}\).

For this digit map, \(\mu=5/3<2\), \(\sigma=\sqrt{26}/3<2\), \(\sqrt2\sigma<3\), and \(2\sigma/\sqrt\mu<3\). The explicit three size conditions (B1)--(B3) preceding Gilmer [1, Theorem 3.5] hold at both indicated lengths. In fact each follows by the following stronger, all-integer inequalities at \(m=136\) and \(m=224\):
\[
\begin{split}
28+12\cdot3^{5m/8}&<3^{m-1},\\
6&<3^{3m/8},\\
8(7+3^{3m/4}+3\cdot3^{5m/8})&<3^{m-1}.
\end{split}
\]
The supplied executable verifies these inequalities directly. They majorize the left sides of (B1), (B2), and (B3), respectively, using the preceding elementary bounds on the digit parameters.

**3. Infinite density transfer.** Gilmer's general theorem [1, Theorem 4.1] yields, for a sufficiently long \(m\)-strict interval \(I\) with density \(d_C(I)\) of numbers eventually entering a chosen union of cycles \(C\), the upper natural density lower bound
\[
\overline d_C\ge d_C(I)\exp\left(-\frac{2}{3^{m/4}-1}-\frac{4\sigma}{\sqrt\mu\,(3^{m/8}-1)}\right).
\]
The theorem applies separately to the basin of \(1\) and to its complement, because all integer trajectories enter finite cycles. At each of our two lengths, the exponential factor exceeds \(1-10^{-6}\), since \(\sigma/\sqrt\mu=\sqrt{26/15}<3/2\) and exact integer comparison gives
\[
\frac{2}{3^{m/4}-1}+\frac{6}{3^{m/8}-1}<10^{-6},
\qquad e^{-x}>1-x\ (x>0).
\]
It follows that
\[
\overline d_{\mathcal H}>\frac{37188}{100000}(1-10^{-6})>0.3718.
\]
Applying the same inequality to the nonhappy basin gives its upper density greater than \((1-110033/1000000)(1-10^{-6})\). Because the two basins partition the positive integers, the lower density of the happy basin is therefore
\[
\underline d_{\mathcal H}<1-
\left(1-\frac{110033}{1000000}\right)(1-10^{-6})<0.11004.
\]
All strict numerical comparisons are certified by rational cross multiplication in the accompanying verifier. The incompatible upper and lower bounds prove the theorem.

## Verification
Run `python3 ternary_happy_density_checker.py` using only the Python standard library. The program constructs the basin table, tests the complete finite reduction, builds the integer polynomial coefficient recurrences, checks small shells independently by direct enumeration, prints both large shell counts, verifies Gilmer's explicit starting conditions by strict integer bounds, and certifies both final density inequalities by integer cross multiplication. It is an exact finite certificate combined with a cited published infinite theorem; the numerical computation alone does not prove any asymptotic conclusion.

## Relationship to prior work
Gilmer [1, Sections 2--5] developed the density-transfer method and proved nonexistence of natural density for decimal square-digit happy numbers, decimal cubic-digit basins, and an example with a nonpower digit rule in base seven. In particular, [1] already supplies the general theorem and the digit-polynomial counting method; neither is claimed as new here. The new specific input is an exact verified pair of distant ternary square-digit shells with contrasting densities, together with the rigorously checked hypotheses that turn those data into the stated **base-three nonexistence** result. Grundman and Teeple [2] study long progressions of generalized happy numbers in small bases, including ternary parity, but do not establish this density dichotomy in their inspected article.

## Limitations
The result does not determine the sharp limsup or liminf, their existence as exact constants, or the full set of subsequential accumulation values. It does not prove a corresponding theorem for other bases or other digit powers. The argument relies on the validity of Gilmer's proven density-transfer theorem, rather than reproving that substantial analytic result. No exhaustive guarantee that an equivalent base-three density result is absent from unindexed literature is asserted; the closely relevant 2022 survey [3] was accessible only at abstract and bibliographic level in this examination. An independent mathematical audit has not been performed.

## References
[1] Justin Gilmer, *On the Density of Happy Numbers*, arXiv:1110.3836 (first public version 2011-10-17), subsequently *Integers* **13** (2013). https://arxiv.org/pdf/1110.3836 — especially Definition 3.1, the hypotheses (B), Theorem 4.1, and the application tables in Section 5.

[2] Helen G. Grundman and Elizabeth A. Teeple, *Sequences of Generalized Happy Numbers with Small Bases*, *Journal of Integer Sequences* **10** (2007), Article 07.1.8. https://cs.uwaterloo.ca/journals/JIS/VOL10/Grundman/grundman5.pdf

[3] Helen G. Grundman and Laura L. Hall-Seelig, *Happy Numbers, Happy Functions, and Their Variations: A Survey*, *La Matematica* **1** (2022), 404–430, DOI:10.1007/s44007-021-00010-x. Abstract and bibliographic details only inspected.
