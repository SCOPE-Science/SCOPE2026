# Exact threefold additive covering of binary Gold graphs beyond differential uniformity

## Finding
For any integers \(m,r\ge1\), let \(q=2^m\), \(g=\gcd(m,r)\), \(s=2^g\), \(n=m/g\), and \(F=\mathbb F_q\). Define the Gold polynomial graph
\[
G_{m,r}=\{(x,x^{2^r+1}):x\in F\}\subset F^2,
\]
with exact iterated additive sumsets \(hG_{m,r}\) (repetitions allowed). Then
\[
\boxed{3G_{m,r}=\begin{cases}G_{m,r},&n=1,\\F\times\mathbb F_s,&n=2,\\F^2,&n\ge3.\end{cases}}
\]
The embedded subfield \(\mathbb F_s\subset F\) in the middle case is canonical. The twofold sumset always has cardinality
\[
\boxed{|2G_{m,r}|=1+(q-1)q/s.}
\]
Consequently, for \(n\ge3\), the least \(h\) with \(hG_{m,r}=F^2\) is exactly \(h=3\); for \(n=1,2\), no finite such \(h\) exists. More precisely, the graphs generate only their indicated proper additive subgroups when \(n=1,2\).

For every odd \(n\), there is also an exact representation law: for \((a,b)\in F^2\), the number of **ordered** triples \((x,y,z)\in F^3\) satisfying
\[
x+y+z=a,\qquad x^{2^r+1}+y^{2^r+1}+z^{2^r+1}=b
\]
is \(q+(q-1)s\) when \(b=a^{2^r+1}\), and \(q-s\) otherwise. For \(n=1\), the latter vanishes, as it must; for odd \(n\ge3\), both values are positive.

## Assumptions and scope
All fields are finite of characteristic two; all sums are in the additive group \(F^2\). An exact \(h\)-fold sum permits the zero graph point, so equality of an exact sumset with \(F^2\) is equivalent to additive covering by at most \(h\) summands. The exponent \(r\) may exceed the field degree \(m\). The quantity \(n=m/\gcd(m,r)\) is the order of Frobenius \(x\mapsto x^{2^r}\) on \(F\). Counts refer to ordered tuples, not unordered decompositions.

## Proof
Write \(D=2^r+1\). The polarization identity in characteristic two is
\[
(u+v)^D=u^D+v^D+B(u,v),\qquad B(u,v)=u^{2^r}v+uv^{2^r}.
\]
For any prescribed first-coordinate sum \(a\), every ordered triple can be written uniquely as \((a+u,a+v,a+u+v)\). Its second-coordinate sum is \(a^D+B(u,v)\). Thus the same difference set \(B(F,F)\) controls the second-coordinate fiber of \(3G\) above every \(a\in F\).

Define the additive polynomial \(L(t)=t^{2^r}+t\). Its kernel is precisely \(\mathbb F_s\), because the fixed field of the \(2^r\)-Frobenius is \(\mathbb F_{2^{\gcd(m,r)}}\). Its image is the relative-trace hyperplane
\[
H=\ker\bigl(\operatorname{Tr}_{F/\mathbb F_s}:F\to\mathbb F_s\bigr).
\]
Indeed, the relative trace annihilates \(L\) since the \(2^r\)-Frobenius generates the cyclic Galois group, and both image and trace kernel have size \(q/s\); the relative trace is surjective because finite fields are separable. Substituting \(u=vt\) for \(v\ne0\) gives \(B(vt,v)=v^D L(t)\). Hence
\[
B(F,F)=\{0\}\cup\bigcup_{v\in F^\times}v^D H.
\]
If \(n=1\), then \(H=\{0\}\), so \(B(F,F)=\{0\}\); here \(x^D=x^2\) in \(F\) and the graph is an additive subgroup.

If \(n\) is odd, \(\gcd(D,q-1)=1\). This is the standard identity \(\gcd(2^r+1,2^m-1)=1\) when \(m/\gcd(m,r)\) is odd: if an odd number \(d>1\) divided both, then \(2^r\equiv-1\pmod d\), while \((2^r)^n=(2^m)^{r/g}\equiv1\pmod d\), contradicting odd \(n\). Thus \(v\mapsto v^D\) permutes \(F^\times\). For odd \(n\ge3\), the hyperplane \(H\) contains a nonzero element, so \(B(F,F)=F\). For odd \(n\), a prescribed nonzero difference \(\Delta\) has exactly \(q-s\) solutions \((u,v)\): each nonzero \(h\in H\) determines a unique \(v\) with \(v^D=\Delta/h\), then exactly \(s\) values of \(u=vt\) lift \(h\). For \(\Delta=0\), \(v=0\) gives \(q\) solutions, and each \(v\ne0\) gives \(s\), proving the stated ordered counts.

Suppose next that \(n\) is even. Write \(h=r/g\), so \(h\) is odd and \(\gcd(h,n)=1\). Then \(\gcd(D,q-1)=s+1\): indeed a common divisor \(t\) of \(s^h+1\) and \(s^n-1\) obeys \(s^h\equiv-1\pmod t\) and \(s^n\equiv1\pmod t\). Bézout gives \(uh+vn=1\) with \(u\) odd, whence \(s\equiv(-1)^u=-1\pmod t\), so \(t\mid s+1\). Conversely, since \(h\) is odd and \(n\) even, \(s+1\) divides both. Therefore \(P=(F^\times)^D\) has index \(s+1\) in the cyclic group \(F^\times\). By the preceding identity, \(B(F,F)=F\) exactly when the trace hyperplane \(H\) meets every coset of \(P\). When \(n=2\), \(H=\mathbb F_s\), while \(P=\mathbb F_s^\times\). Consequently \(B(F,F)=\mathbb F_s\). Also \(x^D\) is the relative norm \(N_{F/\mathbb F_s}(x)\), so the whole graph lies in \(F\times\mathbb F_s\); three summands reach every point of that subgroup.

It remains to prove the nontrivial assertion for every even \(n\ge4\). We give an exact coset argument. If \(n\) has an odd divisor \(e\ge3\), put \(E=\mathbb F_{s^e}\subset F\). Because \(e\) is odd and \(s\) is even,
\[
\gcd(s^e-1,s+1)=1.
\]
The subgroup \(E^\times\) therefore lies in \(P\). For an arbitrary coset representative \(a\ne0\), the map \(E\to\mathbb F_s\), \(z\mapsto\operatorname{Tr}_{F/\mathbb F_s}(az)\), is \(\mathbb F_s\)-linear. Its kernel has dimension at least \(e-1\ge2\), so it contains a nonzero \(z\). Then \(az\in H\cap aP\).

Otherwise \(n\) is a power of two, with \(n\ge4\). Take \(E=\mathbb F_{s^2}\subset F\). Every \(z\in E\) has \(\operatorname{Tr}_{F/\mathbb F_s}(z)=(n/2)\operatorname{Tr}_{E/\mathbb F_s}(z)=0\), since \(n/2\) is even. Thus \(E\subset H\). The image of \(E^\times\) in \(F^\times/P\) has order \(s+1\), so it meets all cosets: writing \(F^\times=\langle\gamma\rangle\), the subgroup \(E^\times\) is generated by \(\gamma^R\), where
\[
R=(q-1)/(s^2-1)=1+s^2+\cdots+s^{n-2}\equiv n/2\pmod{s+1}.
\]
As \(s+1\) is odd and \(n/2\) is a power of two, \(R\) is invertible modulo \(s+1\), hence \(\gamma^R\) generates the quotient. Therefore every coset of \(P\) meets \(E^\times\subset H\). The coset argument proves \(B(F,F)=F\) for all even \(n\ge4\).

Finally, for a twofold sum with first coordinate \(a\ne0\), write the summands as \((au,(au)^D)\) and \((a(1+u),(a(1+u))^D)\). Their second coordinate is \(a^D(1+L(u))\), so it takes exactly \(q/s\) values. At \(a=0\), the sum is necessarily \((0,0)\). Hence \(\lvert2G\rvert=1+(q-1)q/s<q^2\) for every \(q\ge2\), and in the full-covering cases three summands are necessary and sufficient. In the first two cases the graph and all its sums lie in the indicated proper subgroup, so no finite covering order exists. This completes the proof.

## Verification
The standalone script `artifacts/verify_gold.py` constructs polynomial-basis finite fields of orders \(2\) through \(256\) with independently checked irreducible moduli, and enumerates every pair \((u,v)\) for every exponent \(1\le r\le m\) and degree \(1\le m\le8\). It verifies the exact image of \(B\) in each regime, all odd-\(n\) representation counts, the exceptional subfield, and independent twofold-sum cardinalities. It prints `VERIFY_OK exact_gold_cases=36 full_cover_cases=24 odd_fiber_cases=22`. These finite checks corroborate the proof and are not substitutes for its unrestricted field-theoretic arguments.

## Relationship to prior work
Carlet, Gong and Tan [1] analyze differential-uniformity fibers, quadratic functions, and associated strongly regular graphs; their first-public 2014 manuscript motivates the Gold derivative but does not give the general threefold covering threshold as a stated theorem. Thornburgh [2], Theorem 1.6, already gives detailed **three-distinct-point** sum multiplicities for Gold APN graphs when the degree is even and the exponent is coprime to it. That result implies threefold covering in the already-understood APN subfamily for \(m\ge4\), which is **not claimed here as a fresh consequence**. The present complete classification includes the differentially \(s\)-uniform, non-APN regimes \(s>2\) and proves the even-relative-degree \(n\ge4\) cases with a new relative-trace/coset argument. An existing study of Gold graphs' exact fourth Fourier moments [3] determines derivative-fiber sizes and extremizers; its fourth-moment result alone does not imply that every additive target has a threefold representation. These comparisons concern mathematical implications, rather than absence of matching terminology.

## Limitations
The result determines support of exact triple sums in every case and complete ordered triple multiplicities only when \(n\) is odd. It does not give the nonconstant multiplicity spectrum for even \(n\ge4\), nor classify arbitrary quadratic vectorial functions. The APN subfamily's threefold coverage has earlier strong results, and priority for the full non-APN parameter range is not independently certified.

## References
[1] C. Carlet, G. Gong, Y. Tan, *Quadratic Zero-Difference Balanced Functions, APN Functions and Strongly Regular Graphs*, arXiv:1410.2903 (first posted 2014-10-10), especially Sections 2, 3 and 5. https://arxiv.org/abs/1410.2903

[2] D. Thornburgh, *Uniform exclude distributions of Sidon sets*, arXiv:2407.11783 (first posted 2024-07-16), Theorem 1.6. https://arxiv.org/abs/2407.11783

[3] *Exact fourth moments and line-affine phase extremizers for Gold graphs*, research manuscript (2026), proof of the derivative-fiber formula and exact fourth-moment bound. https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-exact-fourth-moments-and-line-affine-phase-extremizers-for-gold--150031da8dce
