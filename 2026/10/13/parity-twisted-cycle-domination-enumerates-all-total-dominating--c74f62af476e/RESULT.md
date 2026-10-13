# Parity-twisted cycle domination enumerates all total dominating sets of cycle prisms
## Finding
For each integer \(n\ge 3\), let the *cycle prism* be \(Y_n=C_n\mathbin{\square} K_2\), with vertex set \(\mathbb Z/n\mathbb Z\times\{0,1\}\). A set \(S\subseteq V(Y_n)\) is *total dominating* when every vertex has an adjacent vertex in \(S\), including vertices belonging to \(S\) themselves. Define its size enumerator
\[
T_n(z)=\sum_{S\text{ total dominating in }Y_n}z^{|S|}.
\]
Let \(D_m(z)\) be the ordinary domination polynomial of the cycle \(C_m\) (the number of sets intersecting each closed neighborhood \(\{i-1,i,i+1\}\), graded by size). **For every \(n\ge3\)**,
\[
\boxed{T_n(z)=\begin{cases}D_{2n}(z),& n\text{ odd},\\ D_n(z)^2,&n\text{ even}.\end{cases}}
\]
This determines **all cardinality coefficients**, not only the total count or minimum size. The cycle polynomial has an explicit finite formula for every \(m\ge3\):
\[
D_m(z)=\sum_{\substack{a,b,c\ge0\\a+2b+3c=m}}
\frac{m(a+b+c-1)!}{a!\,b!\,c!}\,z^{a+b+c}.
\]
In particular \(T_3(z)=z^2(z^4+6z^3+15z^2+14z+3)\), and \(T_4(z)=z^4(z^2+4z+6)^2\).

The equivalent *single rational bivariate formula*, using formal power series at \(t=0\), is
\[
\sum_{n\ge3}T_n(z)t^n=-t\frac{\partial}{\partial t}\log\bigl(A(t,z)B(t,z)C(t,z)\bigr)-z(z+2)t-z^2(z+2)^2t^2,
\]
where
\[
\begin{aligned}
A(t,z)&=1+zt+z^2t^2-z^2t^3,\\
B(t,z)&=1-zt+z^2t^2+z^2t^3,\\
C(t,z)&=1-(2z+z^2)t-z^2t^2-z^2t^3.
\end{aligned}
\]

## Assumptions and scope
All graphs are finite, simple, undirected. The cycle \(C_n\) has \(n\ge3\) distinct vertices. Each prism vertex is \((i,r)\), with \(i\) taken modulo \(n\), \(r\in\{0,1\}\), and open neighborhood
\[
N((i,r))=\{(i-1,r),(i+1,r),(i,1-r)\}.
\]
The ordinary cycle domination polynomial uses *closed* cycle neighborhoods. The bijections below preserve the number of selected vertices and therefore prove the claimed coefficient identities simultaneously for every cardinality. The result does not assert anything for degenerate cycles of length less than three.

## Proof
Write \(x_{i,r}\in\{0,1\}\) for the selection indicator at prism vertex \((i,r)\). Total domination is equivalent to the conjunction, for all \(i,r\), of
\[
x_{i-1,r}\lor x_{i+1,r}\lor x_{i,1-r}=1.\tag{1}
\]
An ordinary dominating set on a cycle, in binary-word form, is precisely a cyclic word having no three consecutive zero entries.

**Odd case.** Assume \(n\) odd. For \(j\in\mathbb Z/(2n)\mathbb Z\), define
\[
y_j=x_{j\bmod n,\,j\bmod 2}.
\]
The Chinese remainder theorem makes this a bijective reindexing of all \(2n\) prism vertex indicators. For any fixed prism vertex \((i,r)\), choose the unique \(j\) with \(j\equiv i\pmod n\) and \(j\equiv1-r\pmod2\). Then
\[
(y_{j-1},y_j,y_{j+1})=(x_{i-1,r},x_{i,1-r},x_{i+1,r}).
\]
As \((i,r)\) varies, \(j\) runs over all residues modulo \(2n\). Thus (1) is exactly the condition that the cyclic word \((y_j)\) contain no \(000\), i.e., it encode an ordinary dominating set of \(C_{2n}\). This bijection preserves all \(2n\) labels and the weight, proving \(T_n(z)=D_{2n}(z)\).

**Even case.** Assume \(n\) even. For \(s\in\{0,1\}\) and \(i\in\mathbb Z/n\mathbb Z\), put
\[
y_i^{(s)}=x_{i,(i+s)\bmod2}.
\]
These are two independent, disjoint reindexings of the \(2n\) vertex indicators. For any prism vertex \((i,r)\), choose \(s\equiv i+1-r\pmod2\). Equation (1) becomes
\[
y_{i-1}^{(s)}\lor y_i^{(s)}\lor y_{i+1}^{(s)}=1.
\]
As \((i,r)\) ranges over vertices, each consecutive-triple condition occurs once in each of the two binary cyclic words. Total domination therefore holds if and only if *both* words are ordinary dominating words on \(C_n\). Their weights add, proving \(T_n(z)=D_n(z)^2\).

**Explicit cycle coefficients.** In a cyclic zero-free word, start at any selected vertex, then advance to the next selected vertex. Each gap, counted inclusive of its initial selected position and exclusive of the next, has length one, two, or three. If these gap lengths occur respectively \(a,b,c\) times, then \(a+2b+3c=m\), with \(k=a+b+c\ge1\) selected vertices. There are \(k!/(a!b!c!)\) ordered gap-length lists and \(m\) choices of a starting position, but every labeled configuration is counted \(k\) times through its possible selected starting vertices. Hence there are \(m(k-1)!/(a!b!c!)\) configurations. Summing yields the displayed formula for \(D_m\).

**Rational form, independently verified.** The length-four-window transfer uses states \((a,b)\), where \(a,b\in\{0,1\}^2\), and a transition \((a,b)\to(b,c)\) is allowed when for both rails \(r\) the Boolean condition \(a_r\lor c_r\lor b_{1-r}=1\) holds; the transition has weight \(z^{|b|}\). Thus the trace of the weighted \(16\times16\) matrix \(W(z)\) raised to the \(n\)-th power equals \(T_n(z)\) for every \(n\ge3\). Exact integer-polynomial elimination through Newton's identities gives
\[
\det(I-tW(z))=A(t,z)B(t,z)C(t,z).
\]
Applying the formal identity \(-t\partial_t\log\det(I-tW)=\sum_{n\ge1}\operatorname{tr}(W^n)t^n\), then subtracting the formal trace terms \(z(z+2)t\) and \(z^2(z+2)^2t^2\), gives the asserted bivariate generating function. The included standard-library verifier reconstructs the transfer, determinant, and traces exactly.

## Verification
The standalone `verify.py` independently constructs the sixteen-state transfer and exact determinant (integer polynomial arithmetic), confirms the cycle formula through cycle length \(120\), and confirms the parity identity through prism order \(60\). It also exhaustively checks all \(1{,}398{,}080\) binary vertex subsets across orders \(3\) through \(10\), comparing **every** coefficient, and compares already-published ungraded and minimum data. Its expected terminal line begins `VERIFY_OK` and reports the actual verification bounds. Exact finite computation corroborates the proof; it is not being treated as the universal argument.

The parity bijections also give exact probability expressions. If prism vertices are selected independently with probability \(p\in(0,1)\), then the probability that the selected set totally dominates is
\[
(1-p)^{2n}T_n\!\left(\frac{p}{1-p}\right),
\]
which the previously available ungraded total alone cannot determine.

## Relationship to prior work
Chaluvaraju and Chaitra's 2014 article introduced and studied total-domination polynomials, with formulas for standard graph families, but not this cyclic-prism parity reduction. The 2016 paper by Hu and coauthors studies total-domination polynomials using several graph identities but does not provide this complete prism distribution.

Azarija, Henning and Klavžar's 2017 *“(Total) Domination in Prisms”* **already establishes the essential bipartite-prism splitting at the level of minimum total domination**. Its proof anticipates the even-order factorization here, so the even branch alone is not claimed as a new structural phenomenon. Its treatment of odd prisms, including a special minimum-value theorem, does not imply an all-cardinality polynomial identity by itself. The new structural point is the one-cycle, double-length **odd-parity** open-to-closed-neighborhood bijection, and its complete coefficient consequences.

OEIS A296102 already tabulates the **ungraded number** \(T_n(1)\) of prism total-dominating sets, and OEIS A303053 already tabulates the number of **minimum-size** sets. OEIS A302405 records the total-domination number. None of these scalar tables gives the all-size polynomial, and no previously known scalar minimum or total is asserted here as novel. The 2015 domination-and-network-reliability thesis by Dod discusses generic graph-polynomial methods; no matching prism cardinality identity was located in the inspected text.

## Limitations
This is a mathematical result with an exact elementary proof, a reproducible symbolic certificate for the optional transfer identity, and bounded exhaustive checks. It does not claim a new total-domination number or new ungraded count. The even-order factorization has strong pre-existing conceptual coverage, and an earlier equivalent expression for the odd-order graded polynomial may exist under neighborhood-hypergraph, covering, or reliability terminology despite targeted searches. Literature priority has **not** been independently certified. No claim is made about generalized prisms with other base graphs or about higher-strength domination.

## References
1. B. Chaluvaraju and V. Chaitra, “Total Domination Polynomial of a Graph” (2014), *Journal of Informatics and Mathematical Sciences*, DOI: `10.26713/jims.v6i2.256`. Public publisher PDF: `https://www.rgnpublications.com/journals/index.php/jims/article/download/256/228/0`.
2. F.-T. Hu et al., “Total domination polynomials of graphs” (2016), arXiv:`1607.00400v1`.
3. J. Azarija, M. A. Henning, S. Klavžar, “(Total) Domination in Prisms” (2017), DOI: `10.37236/6288`.
4. OEIS `A296102` (total dominating sets in prism graphs, ungraded), `A303053` (number of minimum total dominating sets), `A302405` (minimum total domination numbers).
5. M. Dod, “Domination in graphs with application to network reliability” (2015), author-hosted dissertation text.
