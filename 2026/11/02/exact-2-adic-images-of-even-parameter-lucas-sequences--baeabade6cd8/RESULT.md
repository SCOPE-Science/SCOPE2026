# Exact 2-adic images of even-parameter Lucas sequences

## Finding
For any nonzero even integer \(P\), define \(U_0=0\), \(U_1=1\), and \(U_{n+2}=PU_{n+1}+U_n\) for each \(n\ge0\). Write \(h=\nu_2(P)\ge1\). Then the exact closure in the ring of \(2\)-adic integers is
\[
\overline{\{U_n:n\ge0\}}=2^h\mathbb Z_2\;\sqcup\;\bigl(1+2^{2h}\mathbb Z_2\bigr).
\]
In particular, for every positive integer \(N\), the **complete** residue image modulo \(2^N\) is the reduction of these two balls, and its cardinality is
\[
\#\{U_n\bmod 2^N:n\ge0\}
=2^{\max(0,N-h)}+2^{\max(0,N-2h)}.
\]
Its limiting residue density, also the Haar measure of the closure, equals
\[
2^{-h}+2^{-2h}=\frac{2^h+1}{2^{2h}}.
\]
Moreover, the normalized even-index sequence \(U_{2m}/P\) is an exact \(2\)-adic isometry of the nonnegative indices, and a normalized subsequence of the odd indices has the same property.

## Assumptions and scope
The parameter \(P\) is an arbitrary fixed, **nonzero** even integer, including negative values; \(\nu_2(P)\) is the usual exponent of \(2\) in \(|P|\). Index \(n\) and modulus exponent \(N\) are nonnegative and positive integers, respectively. The topology and Haar measure are those of \(\mathbb Z_2\), normalized so \(\mu(\mathbb Z_2)=1\). Only this particular Lucas first-kind sequence with \(Q=-1\) is covered. The separate claims for the two balls establish sufficiency, not merely containment.

## Proof
Put \(u=P^2\), so \(4\mid u\), and \(z=u+2\). Define
\[
f_m=U_{2m}/P,\qquad g_m=U_{2m+1},\qquad H_m=(g_m-1)/u.
\]
These are all integers. Indeed \(U_{2m}\) is divisible by \(P\), and the two-step recurrence gives
\[
f_0=0,\quad f_1=1,\quad f_{m+2}=zf_{m+1}-f_m,\quad
 g_m=f_{m+1}-f_m.
\]
Also \(g_0=1\), \(g_1=1+u\), and \(g_{m+2}=zg_{m+1}-g_m\). Reducing the last recurrence modulo \(u\), the constant sequence \(1\) is a solution with the same initial values, proving \(u\mid g_m-1\) and hence integrality of \(H_m\). Because \(z\) is even, \(f_m\equiv m\pmod2\), so \(g_m=f_{m+1}-f_m\) is odd for every \(m\ge0\). Extend \(f\) to index \(-1\) by \(f_{-1}=-1\).

The elementary addition formulas for a second-order sequence (obtainable by induction from the displayed recurrence) give, for \(n\ge0\) and \(t\ge1\),
\[
\begin{aligned}
f_{n+t}-f_n&=u f_n H_t+f_t(f_n-f_{n-1}),\\
H_{n+t}-H_n&=g_nH_t+f_nf_t.
\end{aligned}
\tag{1}
\]
For the first equality, use \(f_{n+t}=f_n f_{t+1}-f_{n-1}f_t\), \(f_{t+1}=f_t+g_t\), and \(g_t=1+uH_t\). For the second, use the multiplication identity \(g_{n+t}=g_n g_t+u f_n f_t\), subtract \(1\), and divide by \(u\). This multiplication identity follows directly by induction in \(t\), using the same recurrence and the initial values \(g_0=1\), \(f_0=0\).

Define \(v_m=f_{m+1}-f_{m-1}\). The Lucas doubling identity yields \(f_{2m}=f_m v_m\), with \(v_1=z\) and \(v_{2m}=v_m^2-2\). Since \(z\equiv2\pmod4\), induction shows \(v_{2^j}\equiv2\pmod4\) for every \(j\ge0\). Starting with \(f_1=1\), this proves
\[
\nu_2(f_{2^k})=k\quad(k\ge0).
\tag{2}
\]
The standard identity \(U_{2r+1}=U_{r+1}^2+U_r^2\), with \(r=2t\), implies \(g_{2t}=g_t^2+u f_t^2\) and therefore
\[
H_{2t}=2H_t+uH_t^2+f_t^2.
\tag{3}
\]
Here \(H_1=1\), \(H_2=3+u\), and the latter is odd. Applying (3) inductively with (2), the leading term has valuation \(k\) while the other two terms each have valuation at least \(k+1\). Thus
\[
\nu_2(H_{2^k})=k-1\quad(k\ge1).
\tag{4}
\]
Specifically, for the induction step from \(k\) to \(k+1\), the two discarded terms have valuations at least \(2k\), strictly exceeding \(k\), so no cancellation of the leading term is possible.

Set \(t=2^k\) in the first formula (1). For \(k=0\), its first term is divisible by \(4\); for \(k\ge1\), (4) and \(4\mid u\) make that term divisible by \(2^{k+1}\). The second term has valuation exactly \(k\), because \(f_n-f_{n-1}\) is odd and (2) holds. Hence
\[
\nu_2(f_{n+2^k}-f_n)=k\quad(n\ge0,\ k\ge0).
\tag{5}
\]
If \(m>n\) and \(m-n=2^k w\) with \(w\) odd, telescope exactly \(w\) shifts of size \(2^k\). Each summand divided by \(2^k\) is odd, so their odd sum is odd. Consequently
\[
\nu_2(f_m-f_n)=\nu_2(m-n)\quad(m\ne n,\ m,n\ge0).
\tag{6}
\]
For each \(N\), indices \(0\le m<2^N\) therefore give every residue of \(f_m\bmod 2^N\) exactly once. It follows that the closure of all even-index values \(U_{2m}=Pf_m\) is exactly \(P\mathbb Z_2=2^h\mathbb Z_2\).

For the odd-index portion set \(t=2^{k+1}\) in the second formula (1). By (2) and (4), \(f_t\) has valuation \(k+1\) while \(H_t\) has valuation \(k\). Since \(g_n\) is odd,
\[
\nu_2(H_{n+2^{k+1}}-H_n)=k\quad(n\ge0,\ k\ge0).
\tag{7}
\]
Telescope an odd number of such steps, as above, to obtain
\[
\nu_2(H_{2x}-H_{2y})=\nu_2(x-y)\quad(x\ne y,\ x,y\ge0).
\tag{8}
\]
Thus \(H_{2x}\bmod2^N\), for \(0\le x<2^N\), runs through every residue. Since \(U_{4x+1}=g_{2x}=1+uH_{2x}\), this one odd-index subsequence is dense in \(1+u\mathbb Z_2\). Conversely, the earlier divisibility \(g_m-1\in u\mathbb Z\) shows *all* odd-index terms lie in that ball. Therefore their closure is exactly \(1+P^2\mathbb Z_2=1+2^{2h}\mathbb Z_2\).

The even and odd balls are disjoint, since \(h\ge1\). A ball \(a+2^r\mathbb Z_2\) contributes \(2^{\max(0,N-r)}\) distinct residue classes modulo \(2^N\), proving the cardinality formula. The Haar measure is the sum \(2^{-h}+2^{-2h}\). Since each ball is open and closed, their union is already closed, completing the proof.

## Verification
The standalone Python standard-library program `verify.py` independently enumerates the full modular state cycle of the recurrence, compares its attained value set—not only its size—with the two predicted congruence balls, and verifies the exact finite-level cardinality. It additionally checks thousands of valuation-isometry pairs and the doubling identities used in the proof. Successful output: `VERIFY_OK modular_image_cases 216 total_modular_states 76816 isometry_pairs 54432 doubling_identities 1080`. The finite checks support error detection; the induction and telescoping arguments above prove the arbitrary-parameter and arbitrary-precision conclusions.

## Relationship to prior work
Bragman and Rowland, *Limiting density of the Fibonacci sequence modulo powers of a prime* (first public preprint 2022-02-01; arXiv:2202.00704v1), analyze the *ordinary Fibonacci recurrence* \(P=1\), rather than the even-parameter family here. Lang and Lang, *Three term recurrence and residue completeness* (arXiv:1307.7463), classify residue completeness and show the even-parameter family is not complete for moduli divisible by \(4\); noncompleteness alone does not determine the full image, its two constituent balls, or its measure. Sanna, *On the number of residues of linear recurrences* (arXiv:2109.05734), and Accossato and Sanna, *On the number of residues of certain second-order linear recurrences* (arXiv:2401.07661v1), investigate range-size phenomena, including variations of the initial conditions and modulus, rather than this explicit fixed-initial-condition image. The general interpolation framework of Rowland and Yassawi may offer alternative routes to the computation; no novelty is asserted for generic \(p\)-adic recurrence interpolation.

## Limitations
Only \(Q=-1\) and even nonzero \(P\) are proved. Odd \(P\), other \(Q\), odd-prime completions, and distributions of *index multiplicities* inside the balls are not classified. The asserted originality is conditional on the inspected sources; a specialized older recurrence-residue paper might contain an equivalent, unlocated formulation. Numerical experiments are not a substitute for the symbolic proof. No independent audit has been performed.

## References
1. N. Bragman and E. Rowland, *Limiting density of the Fibonacci sequence modulo powers of a prime*, arXiv:2202.00704v1 (2022-02-01), https://arxiv.org/abs/2202.00704.
2. C. L. Lang and M. L. Lang, *Three term recurrence and residue completeness*, arXiv:1307.7463 (2013), https://arxiv.org/abs/1307.7463.
3. C. Sanna, *On the number of residues of linear recurrences*, arXiv:2109.05734 (2021), https://arxiv.org/abs/2109.05734.
4. F. Accossato and C. Sanna, *On the number of residues of certain second-order linear recurrences*, arXiv:2401.07661v1 (2024-01-15), https://arxiv.org/abs/2401.07661.
5. E. Rowland and R. Yassawi, *p-adic asymptotic properties of constant-recursive sequences*, Indagationes Mathematicae 28 (2017), 205–220; cited for methodological context, not asserted as fully inspected.
