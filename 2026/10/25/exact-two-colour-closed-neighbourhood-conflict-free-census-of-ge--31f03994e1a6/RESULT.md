# Exact two-colour closed-neighbourhood conflict-free census of generalized Petersen graphs

## Finding
For every integer \(n\ge3\) and \(1\le k<n/2\), let \(G=\operatorname{GP}(n,k)\). Count maps of all vertices to **two named colours**, red and blue, such that every closed neighbourhood contains a colour occurring exactly once. No proper-colouring requirement is imposed. Set, in \(\mathbb F_2[t]\),
\[
 h_k(t)=t^{k+1}\bigl[1+(t^{-1}+1+t)(t^{-k}+1+t^k)\bigr].
\]
The bracket is a Laurent polynomial but the displayed product is an ordinary polynomial. The **exact number** of valid colourings is
\[
 \boxed{C(n,k)=2^{\deg\gcd_{\mathbb F_2[t]}(t^n+1,h_k(t))}.}
\]
Every such colouring uses both colours. For the ordinary cycle prism \(\operatorname{GP}(n,1)\), this specialises to
\[
 C(n,1)=\begin{cases}2,&n\text{ odd},\\4,&n\equiv2\pmod4,\\16,&4\mid n.\end{cases}
\]
For \(\operatorname{GP}(n,2)\), with \(n\ge5\), it becomes
\[
 \boxed{C(n,2)=\begin{cases}2,&n\text{ odd},\ 5\nmid n,\\4,&n\text{ even},\ 5\nmid n,\\32,&n\text{ odd},\ 5\mid n,\\64,&10\mid n.\end{cases}}
\]
Moreover, the \(\operatorname{GP}(n,2)\) colourings are characterized structurally by five-periodicity of the successive outer-cycle colour differences. Counts **up to swapping the two colour names** are one half of those displayed.

## Assumptions and scope
Write indices modulo \(n\). The cubic graph \(\operatorname{GP}(n,k)\) has outer vertices \(u_0,\ldots,u_{n-1}\), inner vertices \(v_0,\ldots,v_{n-1}\), and edges \(u_i u_{i+1}\), \(u_i v_i\), and \(v_i v_{i+k}\), with \(n\ge3\) and \(1\le k<n/2\). This last restriction ensures every closed neighbourhood has exactly four distinct vertices. The two named colours must be assigned to *every* vertex; the colouring need not be proper. In a four-element neighbourhood, a colour is unique if and only if the number of red vertices is \(1\) or \(3\). In characteristic two this is equivalent to the sum of its four red-indicator bits being \(1\).

## Proof
Let \(x_i\in\mathbb F_2\) and \(y_i\in\mathbb F_2\) be the red indicators on \(u_i\) and \(v_i\), respectively. The condition at every outer vertex is
\[
 x_{i-1}+x_i+x_{i+1}+y_i=1,
\]
so each outer red-bit word \(x=(x_0,\ldots,x_{n-1})\) has **at most one** compatible inner word, explicitly
\[
 y_i=1+x_{i-1}+x_i+x_{i+1}.
\]
The condition at inner vertex \(v_i\) is
\[
 x_i+y_{i-k}+y_i+y_{i+k}=1.
\]
Insert the expression for \(y\). As three constant ones sum to one in \(\mathbb F_2\), the constants cancel, leaving the homogeneous relation
\[
 \bigl[1+(T^{-1}+1+T)(T^{-k}+1+T^k)\bigr]x=0,
\]
where \((Tx)_i=x_{i+1}\) and \(T^n=1\). Thus, no outer word satisfying this relation is lost: its uniquely determined inner word satisfies *every* neighbourhood condition.

Identify cyclic binary words of length \(n\) with the quotient ring \(R_n=\mathbb F_2[t]/(t^n+1)\). Multiplication by \(t\) models cyclic shifting up to reversal convention, which does not alter the kernel size. Since \(t\) is invertible modulo \(t^n+1\), the linear relation has the same kernel as multiplication by \(h_k(t)\). Write \(g=\gcd(t^n+1,h_k(t))\), \(t^n+1=gm\), and \(h_k=ga\), with \(\gcd(a,m)=1\). A residue \(f\pmod{t^n+1}\) is in the kernel exactly if \(gm\mid gaf\), equivalent to \(m\mid f\). There are \(2^{\deg g}\) distinct residues of the form \(m b\pmod{gm}\), proving the general formula even when the modulus has repeated factors.

For \(k=1\), direct expansion gives \(h_1(t)=1+t^4=(t+1)^4\). The multiplicity of \(t+1\) in \(t^n+1\) is \(2^{\nu_2(n)}\) (factor \(n=2^am\) with \(m\) odd and use \((t^m+1)^{2^a}\)). Therefore \(\deg g=\min\{4,2^{\nu_2(n)}\}\), yielding the stated prism cases.

For \(k=2\), expansion gives
\[
 h_2(t)=1+t+t^5+t^6=(1+t)(1+t^5).
\]
In particular, the kernel equation is \((1+T)(1+T^5)x=0\). Set \(z_i=x_i+x_{i+1}\). This relation is equivalent to \(z_{i+5}=z_i\), so the successive differences form a five-periodic word. If \(5\nmid n\), the difference word must be constant because its cyclic periods \(5\) and \(n\) are coprime. It is zero for odd \(n\) (a cyclic word has even total difference sum) and it may be zero or one for even \(n\). Each permissible difference word has exactly two choices for \(x_0\); thus counts are \(2\) and \(4\).

If \(5\mid n\), write \(n=5m\). There are five free difference bits repeated \(m\) times. The cyclic closure condition is \(m(z_0+\cdots+z_4)=0\) in \(\mathbb F_2\). For odd \(m\), exactly \(16\) five-bit patterns satisfy this parity condition, and for even \(m\), all \(32\) do. Each has two choices of initial outer bit, giving \(32\) or \(64\) colourings. The inner bits follow from the outer equation. This proves both the counts and the structural characterization.

The all-red and all-blue assignments have even red parity on each four-element neighbourhood, hence are excluded. Thus every counted map uses both colours and colour swapping acts freely, giving the unlabelled counts.

## Verification
The standalone Python 3 file `checker.py` independently implements the direct closed-neighbourhood definition for all \(2^{2n}\) named-colour maps when \(3\le n\le8\) and all allowed \(k\), exhaustive outer-word enumeration for \(3\le n\le17\) and \(1\le k\le\min\{6,(n-1)/2\}\), and binary polynomial gcd using bitwise integer arithmetic. All tests agreed with the formula. The proof is symbolic and holds for every stated \(n,k\); the finite checks are safeguards, not an extrapolation proof. Run `python3 checker.py` from the extracted package directory. In particular, \(\operatorname{GP}(5,2)\) has \(32\) named valid colourings and \(\operatorname{GP}(10,2)\) has \(64\).

## Relationship to prior work
Sedlar and Škrekovski (2026) use exactly the improper, fully coloured closed-neighbourhood conflict-free notion and show that some planar graphs need four colours, focusing on lower bounds and gadget constructions, not this enumeration. Fabrici, Lužar, Rindošová, and Soták (2022) establish foundational closed-neighbourhood conflict-free bounds, with substantial attention to the additional condition of properness; the present colourings are generally improper. Collins and collaborators (2025) characterize when generalized Petersen graphs admit **balanced** binary closed-neighbourhood colourings, requiring two red and two blue vertices in every four-element neighbourhood. This is disjoint from our requirement of one and three; their structural theorem does not imply this count. The polynomial-gcd census determines all named two-colour closed-neighbourhood conflict-free maps in every generalized Petersen family with the indicated parameters and, for \(k=2\), gives a five-divisibility phase transition not obtained by those statements.

## Limitations
The formula addresses **exactly two named colours** and fully coloured vertices; it does not enumerate colourings using three or more named colours, nor does it address the stronger *proper* conflict-free condition. Historical priority requires independent literature verification. The symbolic proof is direct; the finite program is included for reproducibility only and is not a substitute for it.

## References
1. J. Sedlar and R. Škrekovski, “Four colours are needed for closed-neighbourhood conflict-free colouring of all planar graphs,” arXiv:2610.22559v1, publicly posted 15 October 2026, https://arxiv.org/html/2610.22559v1.
2. I. Fabrici, B. Lužar, S. Rindošová and R. Soták, “Proper conflict-free and unique-maximum colorings of planar graphs with respect to neighborhoods,” arXiv:2202.02570, https://arxiv.org/abs/2202.02570.
3. K. L. Collins et al., “Closed Neighborhood Balanced Coloring of Graphs,” *Graphs and Combinatorics* **41**, 88 (2025), https://doi.org/10.1007/s00373-025-02950-5, especially §5.3.
