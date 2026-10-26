# Dyadic clique strips: identical periodic-orbit censuses with opposite transient behaviour

## Finding
Fix integers \(s\ge2\), \(q\ge2\), and \(n=2^s-1\). Let \(G_{n,q}=P_n\square K_q\) be the Cartesian product of the open \(n\)-vertex path and the \(q\)-vertex complete graph. For each configuration \(x\in\mathbb F_2^{nq}\), synchronously update every vertex to the XOR of the states at its *open* neighbours. Write \(F_{n,q}\) for this linear update.

**Parity-dependent Jordan theorem.** Write \(J_d(\lambda)\) for a single Jordan block of size \(d\) with eigenvalue \(\lambda\), with multiplicities indicated by superscripts. Over \(\mathbb F_2\), the Jordan form of \(F_{n,q}\) is
\[
F_{n,q}\sim
\begin{cases}
J_n(0)\oplus J_n(1)^{\oplus(q-1)},&q\text{ odd},\\
J_{n+1}(1)\oplus J_{n-1}(1)\oplus J_n(1)^{\oplus(q-2)},&q\text{ even}.
\end{cases}
\]
In particular, every eventual period is a power of two, and the maximum primitive period is exactly \(2^s\), for each permitted \(q\).

**Exact recurrent and transient census.** If \(q\) is even, every one of the \(2^{qn}\) configurations is periodic immediately. If \(q\) is odd, precisely \(2^{(q-1)n}\) configurations are periodic initially, and all configurations reach a periodic state within exactly at most \(n\) updates. With \(E_t\) denoting the number whose *first* periodic-entry time is exactly \(t\),
\[
E_0=2^{(q-1)n},\qquad E_t=2^{(q-1)n+t-1}\quad(1\le t\le n).
\]
The bound \(n\) is sharp; exactly one half of all configurations attain it. Thus the probability that a uniformly random initial state is recurrent is \(1\) for even \(q\), and \(2^{-n}\) for odd \(q\).

**Complete primitive-orbit census.** Define \(R=q\) when \(q\) is even and \(R=q-1\) when \(q\) is odd. The number of periodic configurations fixed by the \(2^j\)-th iterate is
\[
B_j=\begin{cases}2^{R2^j},&0\le j<s,\\2^{Rn},&j=s.\end{cases}
\]
There are \(B_0=2^R\) fixed points, and, for each \(1\le j\le s\), exactly
\[
\boxed{\frac{B_j-B_{j-1}}{2^j}}
\]
primitive orbits of length \(2^j\). No other primitive periods occur. Consequently, **the complete primitive-period orbit census is identical for widths \(q\) and \(q+1\) whenever \(q\) is even**, even though the former system is a permutation of all its states and the latter has an exponentially small recurrent fraction and a sharp transient depth \(n\).

**One-column boundary contrast.** With the same clique width \(q\), replacing the \(n=4^r-1\) columns by \(4^r\) columns, for any \(r\ge1\), makes the open-neighbour XOR update reversible for *every* \(q\ge2\). The known Dirichlet Rule 90 nilpotence at the dyadic-minus-one path lengths is used, not asserted as new. The joint clique-width Jordan splitting, paired orbit-census identity and exact all-state transient distributions are the assessed contributions.

## Assumptions and scope
All graphs are simple and loopless. The product edges join adjacent path coordinates with the same clique coordinate or distinct clique coordinates at the same path coordinate. The state field is exactly \(\mathbb F_2\), and updates are synchronous with no self-neighbour input. The dyadic theorem holds for all integers \(s\ge2\) and \(q\ge2\), with no claim for arbitrary strip lengths. The one-column contrast applies to \(n=4^r-1\) and \(n+1=4^r\). Periodic-entry time is the least nonnegative integer \(t\) for which \(F_{n,q}^t x\) lies on a periodic orbit; this differs from the first time a state repeats.

## Proof
**1. The path matrix.** Let \(T_n\) be the binary adjacency matrix of \(P_n\), and put \(f_d(z)=\det(zI+T_d)\), with \(f_0=1\), \(f_1=z\). The continuant identity is \(f_{d+1}=z f_d+f_{d-1}\). Its concatenation formula gives \(f_{2m+1}=f_m(f_{m+1}+f_{m-1})=z f_m^2\). Induction therefore yields \(f_{2^s-1}=z^{2^s-1}\). Moreover \(e_1,T_ne_1,\ldots,T_n^{n-1}e_1\) are linearly independent: the \((j+1)\)-st coordinate of \(T_n^j e_1\) is one and all later coordinates vanish. Hence \(T_n\) is similar to a *single* nilpotent Jordan block \(J_n(0)\), and \(T_n^n=0\) while \(T_n^{n-1}\ne0\).

**2. Product decomposition.** Let \(H_q\) be the all-ones \(q\)-by-\(q\) matrix. The adjacency matrix of \(K_q\) is \(I+H_q\), so
\[
F_{n,q}=T_n\otimes I_q+I_n\otimes(I_q+H_q).
\]
When \(q\) is odd, \(H_q^2=H_q\), and the clique coordinate splits as its one-dimensional constant subspace, where \(I+H_q=0\), and the \((q-1)\)-dimensional zero-sum subspace, where \(I+H_q=I\). This gives one \(J_n(0)\) block and \(q-1\) copies of \(J_n(1)\).

When \(q\) is even, \(H_q^2=0\), \(\operatorname{rank}H_q=1\), and its nilpotent Jordan form is \(J_2(0)\oplus J_1(0)^{\oplus(q-2)}\). Thus \(F_{n,q}=I+N\) for a nilpotent \(N\) made of \(q-2\) copies of \(J_n(0)\) and one Kronecker sum \(J_n(0)\otimes I_2+I_n\otimes J_2(0)\).

**3. The characteristic-two two-block calculation.** Identify the remaining \(2n\)-dimensional space with \(\mathbb F_2[x,y]/(x^n,y^2)\). The Kronecker sum is multiplication by \(x+y\). In characteristic two,
\[
(x+y)^t=x^t+(t\bmod2)x^{t-1}y\quad(t\ge1).
\]
For each \(0\le t<n\), multiplication by \((x+y)^t\) has rank \(2(n-t)\): this is immediate for even \(t\); for odd \(t\), write an element as \(f(x)+yg(x)\) and use the two output coordinates \(x^tf\), \(x^{t-1}f+x^tg\) to see the kernel has dimension \(2t\). Since \(n\) is odd, the rank at \(t=n\) is one, and at \(t=n+1\) zero. These ranks characterize exactly two Jordan blocks of sizes \(n+1\) and \(n-1\). The displayed Jordan theorem follows.

**4. Counting configurations and periods.** A nilpotent block cannot contain a nonzero periodic vector. For odd \(q\), the invertible part has dimension \((q-1)n\), and its nilpotent complement is the single chain \(J_n(0)\). An initial state has entered its recurrent component by time \(t\) precisely when its nilpotent coordinate lies in \(\ker T_n^t\), whose dimension is \(\min(t,n)\). Subtraction of successive cumulative counts proves the exact entry-time distribution. For even \(q\), all blocks are unipotent, so every state is immediately periodic.

For a unipotent block \(I+J_d(0)\), characteristic two gives \((I+J_d(0))^{2^j}=I+J_d(0)^{2^j}\); its fixed space has dimension \(\min(2^j,d)\). In either parity case the complete invertible part contains exactly \(R\) blocks, all of lengths at least \(2^{s-1}\), with total dimension \(Rn\). Therefore the number of points fixed by the \(2^j\)-th iterate is \(B_j\). Successive differences count primitive periodic points, and dividing by their period counts orbits. At \(j=s-1\) not all recurrent states are fixed because \(n>2^{s-1}\), establishing the sharp maximum \(2^s\). Replacing even \(q\) with odd \(q+1\) leaves \(R\) unchanged, proving the paired census identity.

**5. Reversibility after adding one column.** From the same continuant, \(f_d(0)=1\) for even \(d\). The values \(f_d(1)\) follow the repeating pattern \(1,1,0\) with period three in \(d\). Since \(4^r\) is even and congruent to one modulo three, both \(T_{4^r}\) and \(I+T_{4^r}\) are invertible. The odd-clique decomposition in step 2 is therefore invertible. For even \(q\), \(H_q\) is nilpotent and the product matrix is an invertible \((I+T_{4^r})\otimes I\) plus the commuting nilpotent \(I\otimes H_q\), hence is invertible as well. Every map on a finite set that is invertible has every state periodic.

## Verification
The included standalone script `artifacts/verify.py` constructs the graph adjacency matrix from edges without using the proof decomposition, performs exact rank computations over \(\mathbb F_2\), compares every relevant fixed-space dimension and all power ranks for 13 parameter cases, and exhaustively traces 21,056 configurations for four additional cases. It also tests the even one-column reversibility contrast for path lengths four and sixteen. Its actual output is embedded as `artifacts/verification_output.txt`. These finite computations are regression checks, **not** an infinite proof; the argument above establishes the full quantified theorem.

## Relationship to prior work
Finite Dirichlet Rule 90 at lengths one less than a power of two is nilpotent; this was already analyzed by Tadaki and Matsufuji (1993), is detailed in Tadaki's arXiv submission (1994, Appendix A), and is treated in broader boundary-condition form by Voorhees (2007/2008). This established path fact is premise material for step 1. Barbé and von Haeseler (2001) study periodic verticals of linear cellular automata, while Rowland and Yassawi (2012) study automatic sequences realized by linear automata. Neither work gives the finite clique-fibre Jordan classification stated here. Existing period-census results for parity updates on complete multipartite graphs and distance-two Boolean cubes concern different graph families and do not imply the long dyadic-period, paired-width transient dichotomy by graph identification.

The potentially reusable general ingredients are the Cartesian-product Kronecker-sum identity and finite-field Jordan theory. The asserted new content is the explicit parity-specific Jordan structure for this *particular infinite family*, its complete transient and cycle census, and the equality of orbit-count distributions across consecutive even/odd clique widths despite opposite transient behaviour. These claims have only been checked against the cited and accessible literature; no exhaustive historical uniqueness assertion is made.

## Limitations
No statement is made about asynchronous updates, weighted edges, nonbinary alphabets, or arbitrary path lengths. The parity effect depends critically on characteristic two and on \(n=2^s-1\). Prior literature covers the constituent path nilpotence, and a broader unlocated product-Jordan theorem could imply parts of the result. Full historical coverage cannot be certified by search alone. The numerical verifier is finite and does not substitute for the proof. Independent mathematical audit has not been performed.

## References
1. S. Tadaki and S. Matsufuji, *Periodicity in One-Dimensional Finite Linear Cellular Automata*, Progress of Theoretical Physics **89** (1993), 325–331. Full text at https://scispace.com/pdf/periodicity-in-one-dimensional-finite-linear-3lewwl6wjh.pdf.
2. S. Tadaki, *Periodicity of cylindrical linear cellular automata*, arXiv:patt-sol/9412003, submitted 1994-12-15, especially Appendix A. https://arxiv.org/abs/patt-sol/9412003.
3. B. Voorhees, *Representations of Rule 90 and Related Rules for Periodic, Null, and Half-Infinite Boundary Conditions*, Journal of Cellular Automata **3** (2008), 1–25. Public author-uploaded full text available via the article's research page.
4. A. Barbé and F. von Haeseler, *Periodic Patterns in Orbits of Certain Linear Cellular Automata*, DMTCS (2001), https://doi.org/10.46298/dmtcs.2290.
5. E. Rowland and R. Yassawi, *A characterization of p-automatic sequences as columns of linear cellular automata*, arXiv:1209.6008, initially submitted 2012-09-26; Advances in Applied Mathematics **63** (2015), 68–89. https://arxiv.org/abs/1209.6008.
