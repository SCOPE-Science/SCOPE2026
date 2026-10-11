# Complete cycle census for additive-affine helical Yang–Baxter automata

## Finding

**Theorem (exact helical orbit census and affine-rule enumeration).** Fix any integers \(m,N\ge1\). Let \(V=\mathbb F_2^m\) and \(q=|V|=2^m\), with vector addition written additively. Consider all invertible affine functions \(f:V\to V\) of the form \(f(x)=Lx+c\). They satisfy the characteristic-two functional equation
\[
f(x)+f(x+f(y))=f(x+f(y+f(x)))\qquad(x,y\in V)
\]
if and only if \(L^2=I\). Set \(D=I+L\), \(r=\operatorname{rank}D\), and \(v=Dc\). In particular, \(D^2=0\) and \(0\le r\le\lfloor m/2\rfloor\).

For the helical update \(T=T_{N,f}\) defined below, its **full state (sites plus carrier)** satisfies
\[
T^2(x_1,\ldots,x_N,b)=
\begin{cases}
(x_1,\ldots,x_N,b),&N\text{ odd},\\
(x_1+v,\ldots,x_N+v,b),&N\text{ even}.
\end{cases}
\]
Consequently \(T^4=I\) for all \(m,N\), and the exact number of fixed full states is
\[
F=\#\operatorname{Fix}T=
\begin{cases}
q(q/2^r)^N,&c\in\operatorname{im}D,\\
0,&c\notin\operatorname{im}D.
\end{cases}
\]
When \(N\) is odd or \(v=0\), the numbers of primitive cycles of lengths one, two and four are, respectively,
\[
(C_1,C_2,C_4)=\bigl(F,(q^{N+1}-F)/2,0\bigr).
\]
When \(N\) is even and \(v\ne0\), every full state has primitive period four, and
\[
(C_1,C_2,C_4)=\bigl(0,0,q^{N+1}/4\bigr).
\]

For each integer \(r\) from \(0\) through \(\lfloor m/2\rfloor\), the number of rank-\(r\) possibilities for \(D\) is
\[
M_{m,r}={m\brack r}_2{m-r\brack r}_2|\operatorname{GL}(r,2)|,
\]
where \({a\brack b}_2\) denotes the Gaussian binomial coefficient. There are exactly \(q\sum_r M_{m,r}\) admissible invertible affine maps \(f\); among them, exactly
\[
\sum_{r\ge1}M_{m,r}(q-2^{m-r})
\]
have every full state on a four-cycle for every even \(N\). For \(m=4\), the rank counts are \((1,105,210)\), yielding \(5056\) affine admissible maps, of which \(3360\) are of this all-four-cycle kind.

## Assumptions and scope

All maps and ranks are over the additive vector space \(V\) in characteristic two; no multiplicative property of the finite field is used. The site-and-carrier update acts on \(V^{N+1}\). Given \((x_1,\ldots,x_N,b_0)\), for \(j=1,\ldots,N\) define
\[
(x_j',b_j)=R_f(x_j,b_{j-1}),\qquad
R_f(x,b)=(b+f(x+b),x+f(x+b)),
\]
then set \(T(x_1,\ldots,x_N,b_0)=(x_1',\ldots,x_N',b_N)\). This is exactly the helical carrier-sweep convention of Araoka–Tokihiro. The term 'fixed state' includes the carrier, not merely a projected site pattern. A primitive \(k\)-cycle contains \(k\) distinct full states. The counts cover *every* \(m,N\) and every bijective affine \(f\) obeying the given functional equation, but make no claim about arbitrary nonlinear admissible maps.

## Proof

**1. Affine admissibility.** Substituting \(f(x)=Lx+c\) in the functional equation and simplifying in characteristic two gives the identity
\[
(L+L^3)x+(I+L^2)c=0\qquad (x\in V).
\]
Since \(L\) is invertible, this is equivalent to \(L^2=I\), which also makes the constant term vanish. Hence \(D=I+L\) satisfies \(D^2=I+L^2=0\). The equality \(\operatorname{im}D\subseteq\ker D\) implies \(2r\le m\).

**2. Two-sweep formula.** Write \(\delta_j=x_j'+x_j=b_j+b_{j-1}\). Directly from the definition of \(R_f\),
\[
\delta_j=D(x_j+b_{j-1})+c,\qquad
x_j'=x_j+\delta_j,\quad b_j=b_{j-1}+\delta_j.
\]
Applying \(D\) gives \(D\delta_j=Dc=v\), independently of the site and carrier. Consequently \(Db_{j-1}=Db_0+(j-1)v\) and
\[
\delta_j=Dx_j+Db_0+(j-1)v+c.
\]
After the whole sweep, \(Dx_j'=Dx_j+v\) and \(Db_N=Db_0+Nv\). Therefore the increment \(\delta_j'\) in the *second* sweep obeys
\[
\delta_j'=\delta_j+(N+1)v.
\]
The site after two sweeps is \(x_j''=x_j+\delta_j+\delta_j'=x_j+(N+1)v\). The carrier after two sweeps is
\[
b''=b_0+\sum_{j=1}^N(\delta_j+\delta_j')=b_0+N(N+1)v=b_0,
\]
since the integer \(N(N+1)\) is even. In characteristic two, \((N+1)v\) is zero for odd \(N\) and is \(v\) for even \(N\). The displayed formula for \(T^2\) follows. A second application shows \(T^4=I\). In particular \(T\) is bijective, with inverse \(T^3\).

**3. Fixed full states and cycle numbers.** A full state is fixed precisely when every \(\delta_j=0\); this also fixes the final carrier. The increment formula then requires \(Dx_j=Db_0+(j-1)v+c\) for all \(j\). The first two terms on the right belong to \(\operatorname{im}D\); hence solutions exist if and only if \(c\in\operatorname{im}D\). In that case, for each of the \(q\) choices of \(b_0\), every equation has exactly \(|\ker D|=q/2^r\) independent solutions, yielding \(F=q(q/2^r)^N\). If \(v=0\), or if \(N\) is odd, \(T^2=I\), so the remaining full states partition into two-cycles. If \(N\) is even and \(v\ne0\), the map \(T^2\) translates every site by the same nonzero vector; it has no fixed points, so every orbit of \(T\) has primitive period four. Dividing the relevant counts by the orbit lengths gives the formulas.

**4. Enumerating rules.** To specify a square-zero endomorphism \(D\) of rank \(r\), first choose its image \(U\) (\({m\brack r}_2\) choices), then its kernel \(K\supseteq U\) of codimension \(r\) (\({m-r\brack r}_2\) choices), and finally an isomorphism \(V/K\to U\) (\(|\operatorname{GL}(r,2)|\) choices). These data specify \(D\) uniquely. Then \(L=I+D\) is invertible and every one of the \(q\) translations \(c\) satisfies the functional equation. For any given \(D\), the condition \(v=Dc\ne0\) holds for exactly \(q-|\ker D|=q-2^{m-r}\) choices. Summing proves the classification and count. At \(m=4\), \(M_{4,0}=1\), \(M_{4,1}=105\), \(M_{4,2}=210\), and the stated numbers follow.

## Verification

Run `python3 verify.py` using only the Python standard library. The script independently evaluates the functional equation for all invertible binary matrices and all translation vectors in dimensions two and three, enumerates the full finite state transition permutations for every admissible pair and lattice lengths one through three (also four in dimension two), checks the claimed two-sweep action and primitive orbit counts, and enumerates all square-zero operators in dimension four. It reports `VERIFY_OK 846906` and the dimension-four census \((1,105,210)\). These checks corroborate finite cases; all unrestricted quantifiers are established by the proof above.

## Relationship to prior work

Araoka and Tokihiro (arXiv:2602.17148v1, first public February 19, 2026), sections 2.2–2.3, establish the characteristic-two functional equation and supply admissible additive involutions; their section 3.1 defines the helical sweep, and their section 3.2 proves low-field qualitative period-two/four statements. The present result uses those definitions and elementary linear algebra to determine *all full-state primitive orbit counts* for *every affine admissible rule in every binary dimension and lattice length*, and an explicit parity/translation criterion for whether every state has period four. It does not claim the known construction of linear involutions, nor the generic finite-permutation orbit-count identities, as independent contributions. Standard Gaussian-binomial enumeration and existing involution-count tables, including OEIS A053722, are background inputs.

## Limitations

This is a classification of the **additive-affine** subclass, not a proof of the source's proposed period bound for arbitrary nonlinear bijections. It counts full configurations including the carrier, not the possibly shorter projected site patterns. The precise literature-priority comparison with some later auxiliary-work manuscripts and the paywalled journal text remains incomplete, although the freely accessible source preprint was examined in full. No independent scientific validation has been performed.

## References

1. Aoi Araoka and Tetsuji Tokihiro, *Integrable cellular automata on finite fields of order \(2^n\)*, arXiv:2602.17148v1 (public February 19, 2026), https://arxiv.org/html/2602.17148.
2. A. Araoka and T. Tokihiro, version of record, *Mathematical Physics, Analysis and Geometry* 29, 30 (2026), DOI 10.1007/s11040-026-09569-9, https://doi.org/10.1007/s11040-026-09569-9.
3. OEIS A053722, number of involutions in \(\mathrm{GL}(n,2)\), https://oeis.org/A053722 (background rank-aggregate cross-check, not a claim of novelty).
