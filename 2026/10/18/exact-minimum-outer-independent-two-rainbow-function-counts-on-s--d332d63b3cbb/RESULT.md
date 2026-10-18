# Exact minimum outer-independent two-rainbow function counts on sunlet graphs

## Finding
For every integer \(n\ge3\), let \(S_n=C_n\circ K_1\) be the graph obtained by giving each vertex of the cycle \(C_n\) one private pendant neighbor. The colors are the two *named* colors \(1\) and \(2\). An outer-independent two-rainbow dominating function assigns each vertex one of \(\varnothing,\{1\},\{2\},\{1,2\}\), requires the empty-labeled vertices to form an independent set, and requires every empty-labeled vertex to see both colors among its neighbors. Its weight is the total number of assigned colors.

Write \(M_n\) for the number of minimum-weight functions on the fixed labeled graph \(S_n\). Set
\[
T=\begin{pmatrix}2&4&2\\4&2&2\\4&4&2\end{pmatrix},\qquad
B=\begin{pmatrix}6&2\\8&2\end{pmatrix}.
\]
**Theorem (complete optimum census).** For every \(m\ge2\),
\[
M_{2m}=2\operatorname{tr}(T^m)
=2\left((4+2\sqrt5)^m+(4-2\sqrt5)^m+(-2)^m\right).
\]
For every \(m\ge1\),
\[
M_{2m+1}=(2m+1)\begin{pmatrix}2&2&1\end{pmatrix}T^m
\begin{pmatrix}1\\1\\1\end{pmatrix}
=(2m+1)\begin{pmatrix}4&1\end{pmatrix}B^m
\begin{pmatrix}1\\1\end{pmatrix}.
\]
In particular, put \(a_0=5\), \(a_1=42\) and \(a_m=8a_{m-1}+4a_{m-2}\) for \(m\ge2\). Then \(M_{2m+1}=(2m+1)a_m\). The first six values \((M_3,M_4,M_5,M_6,M_7,M_8)\) are \((126,152,1780,1200,21112,10336)\).

The minimum weight \(\gamma_{oir2}(S_n)=2n-\lfloor n/2\rfloor\) is **previously known**; the new claim is the complete multiplicity census and the corresponding characterization of every minimum function. Colors are distinguished and no quotient by graph automorphisms or color reversal is taken.

## Assumptions and scope
All graphs are finite, simple, and undirected. For each index \(i\) modulo \(n\), write \(v_i\) for the cycle vertex and \(u_i\) for its private leaf; the edges are \(v_iv_{i+1}\) and \(v_iu_i\). Empty-vertex domination uses open neighborhoods, not closed neighborhoods. A subset of vertices is independent when no edge joins two of its members. We count functions vertexwise, not orbits of functions under symmetry.

## Proof
**1. Exact description of minimum functions.** This paragraph holds more generally for a finite graph \(H\) without isolated vertices and its one-leaf corona \(H\circ K_1\), with \(N=|V(H)|\). Every original-vertex/private-leaf pair has weight at least one. Moreover, a pair of weight one must have its original vertex empty and its leaf assigned exactly one color: a zero leaf next to a zero original vertex would violate independence, while a zero leaf next to a one-color original vertex would fail the two-rainbow condition. Let \(I\) be the set of original vertices belonging to pairs of weight one. Those original vertices are empty, so \(I\) is independent. Every other pair has weight at least two. Consequently
\[
\omega(f)\ge |I|+2(N-|I|)=2N-|I|\ge2N-\alpha(H).
\]
Take any maximum independent set \(I\) of \(H\). Put \(\varnothing\) on its original vertices, \(\{1\}\) on their private leaves, \(\{2\}\) on all other original vertices, and \(\{2\}\) on all other private leaves. Every original vertex of \(I\) has an original neighbor outside \(I\), since \(H\) has no isolated vertices and a maximum independent set is maximal. Therefore all the zero vertices see both colors. This attains weight \(2N-\alpha(H)\).

Equality in the lower bound forces \(I\) to be a maximum independent set, all its pairs to have weight one, and all other pairs weight two. No additional original vertex can be empty: the set of *all* empty original vertices would then be an independent set strictly larger than \(I\). Thus, on an original vertex outside \(I\), there are precisely five allowable weighted-two configurations:
\[
(\{1\},\{1\}),\quad(\{1\},\{2\}),\quad
(\{2\},\{1\}),\quad(\{2\},\{2\}),\quad
(\{1,2\},\varnothing),
\]
where an ordered pair lists the original-vertex label followed by its leaf label. The three original-vertex states \(s\in\{1,2,12\}\) therefore have multiplicities \(w_1=w_2=2\), \(w_{12}=1\). On every vertex of \(I\), the original label is empty and its leaf label is a singleton. It has two permissible leaf colors exactly when its adjacent original-vertex states together contain both colors; otherwise the leaf color is uniquely forced to supply the missing color. These conditions are also sufficient, proving a bijective classification of *all* minimum functions.

**2. Local transfer rule.** A zero cycle vertex lying between two nonzero original states \(s,t\in\{1,2,12\}\) has
\[
g(s,t)=\begin{cases}1,&s=t=1\ \text{or}\ s=t=2,\\2,&\text{otherwise}\end{cases}
\]
possible singleton leaf labels. Indeed, the neighboring original vertices already provide both colors unless they have the same one-color label. The transfer \(T_{s,t}=g(s,t)w_t\), with states ordered \(1,2,12\), is exactly the displayed matrix \(T\). Multiplying transfers weights each nonzero original vertex once and counts every permissible leaf choice of a zero original vertex once. There is no further condition: every empty leaf is paired with an original vertex carrying both colors, and the zero cycle vertices form an independent set.

**3. Even cycles.** If \(n=2m\) with \(m\ge2\), the only maximum independent sets of \(C_n\) are its two alternating sets. For either choice, the \(m\) nonzero original vertices occur in a cyclic order, separated by \(m\) zero vertices. For \(m=2\), the two zero vertices impose two separate constraints between the same two nonzero vertices; the cyclic transfer still counts both. The transfer weight sum for each independent set is \(\operatorname{tr}(T^m)\). The two sets are disjoint classes of functions, proving \(M_{2m}=2\operatorname{tr}(T^m)\).

**4. Odd cycles.** If \(n=2m+1\) with \(m\ge1\), there are exactly \(n\) maximum independent sets, each formed by an alternating pattern with exactly one adjacent pair of complementary (nonzero) original vertices. For each such independent set, the \(m\) zero vertices impose the transfer constraints along a *path* through all \(m+1\) nonzero original vertices. The first vertex contributes its multiplicity \(w_s\); each subsequent transfer contributes \(g(s,t)w_t\). Summing the endpoint states yields \((2,2,1)T^m(1,1,1)^{\mathsf T}\), independently of the position of the adjacent complementary pair. Multiplication by \(n\) gives the stated odd formula.

**5. Closed forms.** The color-swap-symmetric subspace consists of vectors \((x,x,y)\). On it, \(T\) acts by \(B=\left(\begin{smallmatrix}6&2\\8&2\end{smallmatrix}\right)\); on the antisymmetric line \((x,-x,0)\), its eigenvalue is \(-2\). The characteristic polynomial of \(B\) is \(\lambda^2-8\lambda-4\), with roots \(4\pm2\sqrt5\). Taking traces yields the even closed form. The odd boundary vectors are color-swap symmetric and therefore exclude the \(-2\) mode. Their weighted matrix products satisfy the asserted second-order recurrence with initial values \(5\) and \(42\).

## Verification
The standalone \(\texttt{verify.cpp}\) encodes each vertex label by a two-bit color mask and directly enumerates every assignment on \(S_n\) for \(3\le n\le6\), checking the empty-vertex independence condition and exact two-color union condition. The exhaustive search covers \(17{,}895{,}424\) total assignments, with minimum-weight values and multiplicities agreeing with the theorem in every case. A separate exact-integer transfer-matrix computation checks both displayed recurrence regimes up to cycle order \(51\). Compile using \(\texttt{g++ -std=c++17 -O3 verify.cpp -o verify}\), then run \(\texttt{./verify}\). The output is included in \(\texttt{verify_output.txt}\); no external libraries beyond the usual Boost multiprecision C++ header are required. The infinite-family conclusion is proved above, not inferred from the finite checks.

## Relationship to prior work
Cabrera-Martínez (2022) introduced relevant corona formulas for the *minimum weight* of outer-independent two-rainbow functions when the second factor has no isolated vertices. Samadi and Soltankhah (2022 preprint, Theorem 3.4) supplied the scalar identity \(\gamma_{oir2}(H\circ K_1)=2|V(H)|-\alpha(H)\) for a graph \(H\) without isolated vertices. Their proof exhibits a minimum configuration and the minimum weight but does not count all optimal labelings. The theorem here explicitly retains the four local pure-color choices, the double-color state, and the constraints on empty vertices, producing a full minimum-function census with two parity-sensitive formulas. It refines rather than claims the known scalar result. Other parameters on sunlets, such as power domination, and outer-independent total two-rainbow domination impose different feasibility conditions, so their scalar results do not determine this census.

## Limitations
The formulas count fixed labeled minimum functions only for the ordinary **outer-independent two-rainbow** condition on one-leaf cycle coronas. They do not classify nonminimum functions, unlabeled/color-equivalence orbits, or arbitrary corona factors. Bibliographic searches and full-text comparisons cannot exclude every unindexed equivalent count. Independent mathematical validation and exhaustive priority verification have not been performed.

## References
1. A. Cabrera-Martínez, “A Note on Outer-Independent 2-Rainbow Domination in Graphs,” *Mathematics* **10** (2022), article 2287, first online 2022-06-30. DOI: https://doi.org/10.3390/math10132287. Especially Theorem 6 and the corona section.
2. B. Samadi and N. Soltankhah, “Further results on outer independent 2-rainbow dominating functions of graphs,” arXiv:2208.02340, initial public submission 2022-08-03. See Theorem 3.4 and its proof, pp. 10–11 of https://arxiv.org/pdf/2208.02340.
3. Z. Mansouri and D. A. Mojdeh, “Outer independent rainbow dominating functions in graphs,” *Opuscula Mathematica* **40** (2020), 599–615. DOI: https://doi.org/10.7494/OpMath.2020.40.5.599.
