# Sharp ancillary-qubit minimum for connected two-step mixed circulant rings

## Finding
Let \(n\ge 6\) be even. On \(\mathbb Z/n\mathbb Z\), draw precisely the two directed arcs \(j\to j+a\) and \(j\to j+b\) from every vertex, where \(1\le a<b<n\), the four residues \(\{a,-a,b,-b\}\) are distinct, and \(\gcd(n,a,b)=1\). Thus the underlying undirected graph is a connected simple \(4\)-regular circulant. In the mixed-graph-state commutation-completion framework, let \(e(G)\) denote the least number of ancillary qubits needed to make the associated stabilizer rows commute, in the precise sense of Riera--Parker--Stănică [1, Lemma 4.1].

**Sharp optimization theorem.** Among all such directed two-step rings of order \(n\),
\[
\boxed{\min_{a,b}e(G)=\left\lfloor\frac{n-2}{4}\right\rfloor.}
\]
The minimum is attained for every even \(n\ge6\) by \(a=1\), \(b=n/2-1\). Equivalently, the maximum binary nullity of the underlying connected four-regular circulant adjacency matrix is \(n/2+1\) when \(n\equiv2\pmod4\), and \(n/2+2\) when \(4\mid n\). This is a statement about the *fixed unweighted adjacency matrix over \(\mathbb F_2\)*, not the smallest real or complex rank among matrices sharing a zero pattern.

## Assumptions and scope
All linear algebra defining the ancillary cost is over \(\mathbb F_2\). Put \(A_{j,j+a}=A_{j,j+b}=1\) and all other entries zero, with indices modulo \(n\). The distinct-residue condition rules out loops, reciprocal arcs, and repeated underlying edges. The symmetrized adjacency is \(\Gamma=A+A^{\mathsf T}\); its diagonal vanishes. The undirected graph is connected exactly when \(\gcd(n,a,b)=1\). The known mixed-rank identity [1, Lemma 4.1] gives \(e(G)=\frac12\operatorname{rank}_{\mathbb F_2}(\Gamma)\), an integer because \(\Gamma\) is alternating. Optimization is over the stated directed two-step family and the stated commutation-completion notion only; no assertion is made about unrelated circuit architectures or minimum ranks over other fields.

For a positive integer \(d\), write \(\nu_2(d)\) for its exponent of \(2\). Let
\[
 n=2^t m,\quad m\ \text{odd},\quad s=2^t,\quad u=b-a,\quad v=a+b,
\]
\[
 p=\nu_2(u),\quad q=\nu_2(v),\quad r_u=\gcd(m,u),\quad r_v=\gcd(m,v).
\]
Here \(t\ge1\), \(u,v>0\), and connectedness implies \(\gcd(r_u,r_v)=\gcd(m,u,v)=1\).

## Proof
**1. Exact finite-field nullity lemma.** In the cyclic group algebra \(\mathbb F_2[x]/(x^n-1)\), multiplication by the Laurent polynomial of \(\Gamma\), after multiplication by the unit \(x^b\), is multiplication by
\[
 x^b\bigl(x^a+x^{-a}+x^b+x^{-b}\bigr)
 =(1+x^{b-a})(1+x^{a+b}).
\]
For any polynomial \(f\), the kernel of multiplication by \(f\) modulo \(x^n-1\) has dimension \(\deg\gcd(f,x^n-1)\). To see this, if \(d=\gcd(f,x^n-1)\), write \(f=df_1\), \(x^n-1=dh_1\) with \(\gcd(f_1,h_1)=1\); then \(fh=0\) modulo \(x^n-1\) exactly when \(h_1\mid h\), yielding \(\deg d\) free coefficients.

In characteristic two, \(x^n-1=(x^m+1)^s\), while \(1+x^u\) is the \(2^p\)-th power of a squarefree odd-exponent polynomial, and likewise for \(v\). Among roots of \(x^m+1\) that annul at least one factor, exactly \(r_u-1\) annul only \(1+x^u\), \(r_v-1\) annul only \(1+x^v\), and one root annuls both; all remaining roots annul neither and contribute zero to the gcd degree. Here the intersection has one root since \(\gcd(m,u,v)=\gcd(m,a,b)=1\) (\(m\) is odd). Taking the minimum of multiplicities with \(s\) proves the exact identity
\[
 \kappa:=\operatorname{nullity}_{\mathbb F_2}(\Gamma)
 =(r_u-1)\min(s,2^p)+(r_v-1)\min(s,2^q)
 +\min(s,2^p+2^q).
 \tag{1}
\]
This is valid without assuming \(p,q<t\). Consequently \(e(G)=(n-\kappa)/2\).

**2. Universal upper bound on binary nullity.** We show
\[
\kappa\le\begin{cases}n/2+1,&n\equiv2\pmod4,\\n/2+2,&4\mid n.\end{cases}\tag{2}
\]
Because \(\gcd(r_u,r_v)=1\) and both divide \(m\), the product \(r_ur_v\) divides \(m\). If \(a,b\) have opposite parity, then \(u,v\) are odd and (1) gives \(\kappa=r_u+r_v\le r_ur_v+1\le m+1\), which implies (2) for every \(t\ge1\).

If \(a,b\) have the same parity, connectedness forces both to be odd. Then \(u,v\) are even and *exactly one* of \(p,q\) equals \(1\), while the other is at least \(2\): the two integers \((b-a)/2\) and \((a+b)/2\) have opposite parities. If \(t=1\), both factors in (1) saturate the modulus multiplicity \(s=2\), so \(\kappa=2(r_u+r_v-1)\). Both \(r_u,r_v\) are proper odd divisors of \(m\): if \(m\) divided the corresponding even value \(u\) or \(v\), then \(n=2m\) would divide that value, contradicting respectively \(0<u<n\) or \(v\ne n\) with \(0<v<2n\). If one divisor is \(1\), the other is at most \(m/3\), giving \(\kappa\le 2m/3\le m+1\). If both are at least \(3\), then
\[
 2(r_u+r_v-1)\le r_ur_v+1\le m+1,
\]
where the first inequality is \((r_u-2)(r_v-2)\ge1\). Thus (2) holds for \(t=1\).

Suppose \(t\ge2\), and rename the two odd-part divisors as \(R\) for the factor of \(2\)-adic exponent \(1\), and \(S\) for the factor of exponent \(q\ge2\). By coprimality \(RS\le m\). If \(q<t\), (1) reduces to \(\kappa=2R+2^q S\), hence
\[
 \kappa\le 2R+(s/2)m/R \le (s/2)m+2.
\]
The last inequality holds because the convex function \(x\mapsto2x+(s/2)m/x\) on \([1,m]\) has its maximum at an endpoint, and the two endpoint values satisfy \(2+(s/2)m\ge2m+s/2\) since \((s/2-2)(m-1)\ge0\).

If \(q\ge t\), (1) becomes \(\kappa=2R+sS-2\). The divisor \(S\) is proper: otherwise its even underlying shift \(u\) or \(v\), having \(\nu_2\ge t\), would be a multiple of \(n\), forbidden by the distinct-residue hypotheses. If \(S=1\), then
\[
\kappa\le2m+s-2\le(s/2)m+2,
\]
because \((s/2-2)(m-2)\ge0\); the case \(m=1\) is impossible here since it would force that forbidden multiple of \(n\). If \(S\ge3\), then \(R\le m/3\) by coprimality and \(S\le m/3\) because \(S\) is a proper odd divisor, whence
\[
\kappa\le (s+2)m/3-2\le(s/2)m+2
\]
for \(s\ge4\). This proves (2) for all connected admissible rings, and therefore the claimed lower bound on \(e(G)\).

**3. Sharpness for every even order.** Set \(n=2h\), \(a=1\), \(b=h-1\). For \(h\ge3\) the four residues are distinct and the unit step guarantees connectivity. Here \(u=h-2\), \(v=h\), and the odd parts satisfy \(r_u=1\), \(r_v=m\). If \(h\) is odd, \(t=1\), \(p=q=0\), so (1) yields \(\kappa=h+1\). If \(h\equiv2\pmod4\), \(t=2\), \(\nu_2(v)=1\), \(\nu_2(u)\ge2\), hence (1) gives \(\kappa=2m+2=h+2\). If \(4\mid h\), \(t\ge3\), \(\nu_2(u)=1\), \(\nu_2(v)=t-1\), hence (1) gives \(\kappa=2+2^{t-1}m=h+2\). All cases attain (2); dividing the complementary rank by two yields the boxed minimum.

## Verification
The standalone standard-library file `artifacts/verify.py` independently constructs the \(0\)-\(1\) adjacency bit rows and performs Gaussian elimination over \(\mathbb F_2\), comparing every admissible connected step pair against the cyclic-factor nullity formula. It exhaustively checked \(21{,}152\) step pairs on every even order from \(6\) through \(72\), verified the universal bound, and verified the construction at each order. Exact rational matrix ranks at \(n=6,10,12,20\) also distinguish the fixed binary-rank problem from ordinary spectral nullity. None of the finite computations substitutes for the preceding all-order proof. Run `python3 artifacts/verify.py` from the extraction directory.

## Relationship to prior work
Riera, Parker and Stănică [1, Lemma 4.1] already establish the general \(e=\operatorname{rank}_{\mathbb F_2}(A+A^{\mathsf T})/2\) identity. We do not claim that identity. Damnjanović [2, Theorem 14 and Table 4] completely determines **real/complex** nullity maxima among connected quartic circulant adjacency matrices. Its extremal step condition already includes \(a+b=n/2\), so the explicit extremal family is not new as an unweighted real-spectral graph. The present claim instead identifies the optimum **binary** commutation rank for all even orders. In particular, at \(n=12\) the witness \(a=1,b=5\) has real nullity \(6\) but binary nullity \(8\); the real bound cannot imply this binary outcome. Williams [3] analyzes integer Smith forms for selected circulant families, and Deaett--Meyer [4] studies free-parameter Hermitian minimum circulant rank rather than the fixed binary adjacency rank. Neither gives this all-order binary resource optimum. The characteristic-two repeated-root calculation and exact optimization are the contributions asserted here.

## Limitations
The optimization is restricted to connected oriented rings with exactly two outgoing shifts and no reciprocal arc pairs; other mixed graphs or different adjacency patterns may require fewer qubits. The result concerns commutation completion as defined in [1], not a universal gate-complexity or physical-memory lower bound. Binary nullity must not be confused with nullity over \(\mathbb Q\), \(\mathbb R\), or \(\mathbb C\). No uniqueness of the optimizing pair is claimed. A differently formulated binary-rank theorem in weakly indexed literature remains a possible overlap risk.

## References
[1] C. Riera, M. G. Parker, and P. Stănică, *Quantum states associated to mixed graphs and their algebraic characterization*, Advances in Mathematics of Communications 17 (2023), 660--680; early access 2021-05-10, DOI:10.3934/amc.2021015. Author-hosted full text: https://faculty.nps.edu/pstanica/research/2021AMCNewMixed.pdf.

[2] I. Damnjanović, *On the nullities of quartic circulant graphs and their extremal null spaces*, arXiv:2212.12959 (first posted 2022-12-25), Theorem 14, Table 4: https://arxiv.org/pdf/2212.12959.

[3] G. Williams, *Smith forms for adjacency matrices of circulant graphs*, author manuscript (2014): https://repository.essex.ac.uk/8578/1/SNRcirculantgraphs.pdf.

[4] L. Deaett and S. A. Meyer, *The minimum rank problem for circulants*, Linear Algebra and its Applications (2016), arXiv:1511.07920: https://arxiv.org/html/1511.07920v1.
