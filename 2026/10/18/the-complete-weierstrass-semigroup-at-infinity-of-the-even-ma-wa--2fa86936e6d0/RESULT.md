# The complete Weierstrass semigroup at infinity of the even Ma–Wang maximal curves

## Finding
For every prime power \(q>2\) and every even integer \(n\ge4\), let \(X_{q,n}\) be the smooth projective Ma–Wang curve with function field
\[
z^{q^n+1}=c(u^q-u)\bigl(1+(u^q-u)^{q-1}\bigr)^{(q^{n-1}-1)/(q-1)},
\]
over \(k=\mathbb F_{q^{2n}}\), where \(c\ne0\) and \(c^{q^n}=-c\). Write \(P_\infty\) for its unique point over the pole of \(u\). Set
\[
Q=q^n,\quad N=Q+1,\quad b=q(q-1),\quad
K=\frac{q(q^{n-2}-1)}{q^2-1},\quad
m=\frac{q^2(q^{n-1}+1)}{q+1}.
\]
Then the **complete** geometric and \(k\)-rational one-point Weierstrass semigroup is
\[
\boxed{H(P_\infty)=\langle m,m+b,m+2b,\ldots,m+Kb,N\rangle,\qquad m+Kb=Q.}
\]
This displayed set is the *minimal* generating set. Therefore the multiplicity is \(m\) and the embedding dimension is \(K+2\). The conductor and genus are
\[
\boxed{\mathrm c(H)=qm+(b-1)Q},\qquad
\boxed{g(H)=\frac{(q^2-1)Q}{2}=g(X_{q,n})}.
\]
In particular
\[
2g(H)-\mathrm c(H)=q^2(q-1)K>0,
\]
so none of these Weierstrass semigroups is symmetric. An explicit Apéry set with respect to \(N\) is
\[
\boxed{\operatorname{Ap}(H,N)=\left\{qj+b(jr\bmod N):0\le j<N\right\}},
\qquad r=\frac{q^{n-1}-1}{q-1},
\]
where \(jr\bmod N\) is the least nonnegative residue.

## Assumptions and scope
The base \(q\) is an arbitrary prime power greater than two (including powers of two), and \(n\) is even and at least four. The smooth projective curve is the normalization of the indicated Kummer model. The point \(P_\infty\) is rational over \(k\); hence pole orders exhibited by \(k\)-rational functions and the geometric semigroup coincide. All semigroup calculations are exact and uniform in both parameters. This result concerns this point, not the semigroups at arbitrary points of \(X_{q,n}\).

## Proof
**1. Input valuations and arithmetic identities.** Put \(A(T)=T^q-T\), \(B(T)=1+A(T)^{q-1}=(T^{q^2}-T)/(T^q-T)\), and \(r=(q^{n-1}-1)/(q-1)\). In the originating paper, Lemma 2.3 and Proposition 2.4 establish
\[
(u)_\infty=NP_\infty,\quad (z)_\infty=QP_\infty,\quad
\deg B=b,\quad g(X_{q,n})=\frac{(q^2-1)Q}{2}.
\]
The \(b\) roots of \(B\), namely the elements of \(\mathbb F_{q^2}\setminus\mathbb F_q\), are distinct. As \(n\) is even, the curve is totally ramified of index \(N\) at each of them. At the unique point above such a root, \(v(z)=r\) and \(v(B(u))=N\). At a root of \(A\), \(v(z)=1\) and \(B\) is a unit. In particular these statements remain true in even characteristic. Direct integer manipulations give
\[
N=br+q+1,\quad r=1+(q+1)K,\quad
j_0=1+bK,\quad rj_0=1+KN,
\]
\[
m=qj_0+b=N-j_0=Q-bK,\quad \gcd(r,N)=1.
\]
For the gcd, use \(N=br+q+1\) and \(r\equiv1\pmod{q+1}\).

**2. A complete Apéry set by explicit rational functions.** For each integer \(0\le j<N\), set \(e_j=\lfloor jr/N\rfloor\), \(a_j=jr-Ne_j\), and define
\[
f_j=\frac{z^j}{B(u)^{e_j}}.
\]
At the roots of \(B\), \(v(f_j)=jr-Ne_j=a_j\ge0\). At roots of \(A\), the numerator has nonnegative valuation and the denominator is a unit. At all other finite points neither \(z\) nor \(B\) produces a pole. Thus \(f_j\) has no finite poles. At \(P_\infty\) its pole order is
\[
w_j=jQ-bNe_j=qj+b(jr\bmod N),
\]
using \(Q=br+q\). Consequently every \(w_j\) is a nongap, as is \(N\) by the function \(u\). The residues \(w_j\equiv-j\pmod N\) are pairwise distinct. Moreover, for \(0\le i,j<N\), writing \(s=(i+j)\bmod N\), both \(i+j-s\) and \(a_i+a_j-a_s\) are nonnegative multiples of \(N\). Hence \(w_i+w_j-w_s\) is a nonnegative multiple of \(N\). Therefore
\[
S=\bigcup_{j=0}^{N-1}(w_j+N\mathbb Z_{\ge0})
\]
is a numerical semigroup contained in \(H(P_\infty)\), with \(\operatorname{Ap}(S,N)=\{w_j\}\). Because multiplication by \(r\) permutes residues modulo \(N\), the Apéry gap-counting formula yields
\[
\begin{aligned}
\#(\mathbb Z_{\ge0}\setminus S)
&=\frac{1}{N}\sum_{j=0}^{N-1}w_j-\frac{N-1}{2}\\
&=\frac{(q+b-1)(N-1)}2
=\frac{(q^2-1)Q}{2}=g(X_{q,n}).
\end{aligned}
\]
The Weierstrass gap theorem says \(H(P_\infty)\) has exactly \(g(X_{q,n})\) gaps. Since \(S\subseteq H(P_\infty)\) and their complements have equal finite cardinality, \(S=H(P_\infty)\). This establishes the complete Apéry formula independently of any basis assertion.

**3. Minimal generators via a two-dimensional lattice fan.** Consider the index-\(N\) lattice
\[
\Lambda=\{(j,a)\in\mathbb Z^2:a\equiv rj\pmod N\}.
\]
Besides \(E_0=(N,0)\) and \(E_\infty=(0,N)\), define \(G_k=(j_0-bk,1+(q+1)k)\) for \(0\le k\le K\). The identities of step 1 imply \(G_k\in\Lambda\) and \(G_K=(1,r)\). The consecutive rays have determinants
\[
\det(E_0,G_0)=N,\quad
\det(G_k,G_{k+1})=N\ (0\le k<K),\quad
\det(G_K,E_\infty)=N.
\]
All coordinates are nonnegative and the ordered rays sweep the first quadrant, so every lattice point of \(\Lambda\cap\mathbb Z_{\ge0}^2\) belongs to one of the sectors between successive rays. Each adjacent pair is a \(\mathbb Z\)-basis of \(\Lambda\), because its determinant is the lattice index \(N\). A point in a sector is therefore a *nonnegative integral* combination of that sector's two boundary rays. The linear weight \(L(j,a)=qj+ba\) sends \(E_0,E_\infty\) to multiples of \(N\), and sends \(G_k\) to \(m+bk\). Applying this to every \((j,a_j)\) shows that every \(w_j\) is generated by \(N\) and the displayed progression. Conversely, each progression element is \(w_{j_0-bk}\), since both coordinates of \(G_k\) lie in \([0,N-1]\), and is a nongap; this proves the generator description. Finally \(m=q(Q+q)/(q+1)\) gives \(2m>N\) for \(q>2\), whereas \(m\le m+bk\le Q<N\). Thus no proposed generator is the sum of two positive nongaps. All \(K+2\) generators are minimal and \(m\) is the multiplicity.

**4. Maximum Apéry element and conductor.** The identity \(j_0=N-m\) gives \(rm\equiv-1\pmod N\), so \(a_m=Q\) and \(w_m=qm+bQ\). For \(0\le j\le m\), this is at least \(w_j\) termwise. For \(j>m\), write \(h=j-m=bk+t\), where \(0\le t<b\), \(1\le h\le bK\), and let \(s=Q-a_j\). If \(t=0\), then \(s=k(q+1)\) and \(qh-bs=-bk<0\). If \(t>0\), necessarily \(k<K\) and
\[
s=N-tr+k(q+1)\ge N-(b-1)r=r+q+1>qK.
\]
Since \(h\le bK=q(q-1)K\), we have \(qh-bs=q[h-(q-1)s]<0\). Thus \(w_m\) is the unique largest Apéry member. The conductor formula \(\mathrm c(H)=\max\operatorname{Ap}(H,N)-N+1\) becomes \(qm+(b-1)Q\). Subtracting from twice the known genus gives \(2g-\mathrm c=q(Q-m)=qbK=q^2(q-1)K>0\). A numerical semigroup is symmetric exactly when its conductor equals twice its genus; hence this family is non-symmetric.

## Verification
The accompanying dependency-free `verify_semigroup.py` computes all Apéry values exactly, checks the defining integer identities, and compares the explicit Apéry set to independently computed shortest weights on the finite residue graph of the proposed generators. Its tested cases are \((q,n)=(3,4),(4,4),(5,4),(3,6),(4,6),(3,8)\); each passed. For example, \(q=3,n=4\) gives
\[
H(P_\infty)=\langle63,69,75,81,82\rangle,\quad
(g,\mathrm c)=(324,594).
\]
For \(q=4,n=4\), the generators are \(208,220,232,244,256,257\), with genus \(1920\) and conductor \(3648\). The finite checks are corroboration only: the proof above covers every admitted prime power and even exponent.

## Relationship to prior work
Ma and Wang introduced the even-exponent maximal curves and proved their genus and Kummer ramification. **Their Lemma 4.1 already exhibits the individual nongaps** \(N\) and \(Q-bk\) for \(0\le k\le K\), through the functions \(u\) and \(z(z^b/B(u))^k\). This establishes the entire proposed generator list as *nongaps*, but it does **not** establish that those nongaps generate the complete semigroup, or determine its conductor, minimality, embedding dimension, Apéry set or symmetry. The new step is the exact genus-saturation proof, followed by the lattice-fan generator classification and conductor calculation. Montanucci and Pallozzi Lavorante determined the semigroups of the **odd-exponent** second generalized GK curves, including an analogous arithmetic progression at their ideal points (Theorem 1.1, 2019 preprint). The earlier odd-exponent theorem is acknowledged; it does not imply the result here, because the even-exponent family has distinct Kummer ramification \(\gcd(r,N)=1\) at the \(B\)-zeros and did not appear in that paper. General Apéry-set and Kummer-cover techniques form the background, not a claim of new technique. The distinguishing assertion here is the exact complete semigroup of the new even-exponent family, with uniform minimality, conductor and non-symmetry.

## Limitations
Existence of the individual arithmetic-progression nongaps is already in Ma–Wang Lemma 4.1; the present classification proves completeness and the exact minimal/conductor data. The theorem concerns only the unique point \(P_\infty\), and it does not determine one-point code parameters or Weierstrass semigroups at other rational places. It assumes \(q>2\) and even \(n\ge4\). The conclusion relies on the originating paper's verified ramification and genus, and is not an independent re-proof of maximality. No claim of independent verification or exhaustion of unindexed literature is made. A general semigroup result under a different Kummer presentation might subsume the explicit formula; no such covering statement was identified in the inspected sources.

## References
1. L. Ma and Y. Wang, *A new family of maximal curves not covered by the Hermitian curve*, arXiv:2609.19546v1 (first public 2026-09-17), especially equation (2.1), Lemma 2.3, Proposition 2.4 and Lemma 4.1. https://arxiv.org/abs/2609.19546
2. M. Montanucci and V. Pallozzi Lavorante, *AG codes from the second generalization of the GK maximal curve*, arXiv:1901.08897v1 (2019), Theorem 1.1 and Section 3; Discrete Mathematics 343 (2020), 111810. https://arxiv.org/abs/1901.08897
3. H. Stichtenoth, *Algebraic Function Fields and Codes*, 2nd ed., Graduate Texts in Mathematics 254, Springer (2009), Kummer extensions and the Weierstrass gap theorem.
