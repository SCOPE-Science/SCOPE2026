# Exact fibers and all moments of triangular residues modulo arbitrary integers

## Finding
For every integer \(m\ge1\), set \(T(n)=n(n+1)/2\) and define the complete-period fiber
\[
M_m(t)=\#\{0\le n<2m:T(n)\equiv t\pmod m\}\quad(t\in\mathbb Z/m\mathbb Z).
\]
Write \(m=2^\alpha q\), where \(\alpha\ge0\) and \(q=\prod_{p\text{ odd}}p^{a_p}\). For an odd prime power \(p^a\) let \(r_{p^a}(D)\) be the number of square roots of \(D\pmod{p^a}\). Then the following **complete fiber formula** holds, without exceptions:
\[
\boxed{M_m(t)=2\prod_{p^a\parallel q}r_{p^a}(1+8t).}
\]
For each odd \(p\), writing \(d=D\bmod p^a\), the local factor is explicit:
\[
r_{p^a}(D)=\begin{cases}
p^{\lfloor a/2\rfloor},&d=0,\\
2p^j,&v_p(d)=2j<a\text{ and }(d/p^{2j}\bmod p)\text{ is a nonzero square},\\
0,&\text{otherwise}.
\end{cases}
\]
The valuation in the second line is of the unique integer representative \(1\le d<p^a\); \(v_p(0)\) is not used.

More strongly, all positive integer power moments of the fibers admit one local product. For any integer \(k\ge1\), define
\[
C_{p,a}(k)=p^{k\lfloor a/2\rfloor}+2^{k-1}(p-1)p^{a-1}
\sum_{j=0}^{\lfloor(a-1)/2\rfloor}p^{(k-2)j}.
\]
Then
\[
\boxed{\sum_{t\bmod m}M_m(t)^k=2^{k+\alpha}\prod_{p^a\parallel q}C_{p,a}(k).}
\]
In particular, the full-period ordered collision count is
\[
\boxed{\sum_{t\bmod m}M_m(t)^2=4m\prod_{p^a\parallel q}\left(1+a\left(1-\frac1p\right)\right).}
\]
All empty products are \(1\), including \(m=1\).

Let \(R_{p^a}\) count square residue classes (including zero) modulo an odd prime power. Then
\[
R_{p^a}=\begin{cases}
\dfrac{p^{a+1}+2p+1}{2(p+1)},&a\text{ odd},\\
\dfrac{p^{a+1}+p+2}{2(p+1)},&a\text{ even}.
\end{cases}
\]
Consequently the number and the fraction of residues attained by triangular numbers modulo \(m\) are respectively
\[
\boxed{|\operatorname{im}(T\bmod m)|=2^\alpha\prod_{p^a\parallel q}R_{p^a},\qquad
s_m=\prod_{p^a\parallel q}\frac{R_{p^a}}{p^a}.}
\]
These formulas establish both saturation formulas stated as Conjectures 1 and 2 in Ulness (2022): the alternating prime-power expressions and \(s_{2^\alpha q}=s_q\) for odd \(q\).

## Assumptions and scope
All moduli \(m\) are positive integers and all exponents \(a\) and moment orders \(k\) are positive integers. Primes appearing in the local products are odd. The source's multiplicity lists use the first \(m\) indices, whereas \(M_m\) deliberately uses the entire, universally valid \(2m\)-period; this distinction is essential for even moduli. The saturation \(s_m\) counts residues in either index window because both have the same support.

## Proof
**1. Dyadic factor.** For \(\alpha\ge1\), consider \(T:\mathbb Z/2^{\alpha+1}\mathbb Z\to\mathbb Z/2^\alpha\mathbb Z\). For any integers \(u,v\),
\[
2\bigl(T(u)-T(v)\bigr)=(u-v)(u+v+1).
\]
The two factors on the right have opposite parity. Hence \(T(u)\equiv T(v)\pmod{2^\alpha}\) if and only if \(u\equiv v\pmod{2^{\alpha+1}}\) or \(u\equiv-v-1\pmod{2^{\alpha+1}}\). These are distinct classes because \(2u+1\) is odd. Thus every nonempty dyadic fiber consists of exactly two indices. Pairing by \(u\leftrightarrow-u-1\) partitions the \(2^{\alpha+1}\) inputs into \(2^\alpha\) distinct fibers; there are exactly \(2^\alpha\) outputs, so the map is onto and every dyadic fiber equals two. For \(\alpha=0\), the dyadic modulus is \(1\) and the twice-long index period supplies exactly the same overall factor of two.

**2. Odd prime powers.** The identity
\[
(2n+1)^2=8T(n)+1
\]
transforms \(T(n)\equiv t\pmod{p^a}\) into \(x^2\equiv1+8t\pmod{p^a}\), where \(x=2n+1\). Since \(2\) is invertible modulo odd \(p^a\), this change of variable is bijective. If \(D\equiv0\pmod{p^a}\), a root requires \(v_p(x)\ge\lceil a/2\rceil\), giving \(p^{\lfloor a/2\rfloor}\) roots. For \(v_p(D)=2j<a\), write \(x=p^jy\). An odd-prime unit \(D/p^{2j}\) has two roots modulo \(p^{a-2j}\) exactly when it is a nonzero quadratic residue modulo \(p\), by elementary Hensel lifting (derivative \(2y\not\equiv0\pmod p\)); each root has \(p^j\) lifts to a root \(x\pmod{p^a}\). If the valuation is odd or the unit is a nonsquare there are no roots. This proves the local fiber formula.

**3. Chinese remaindering.** The complete index range is a residue system modulo \(2m=2^{\alpha+1}q\), and the target \(\mathbb Z/m\mathbb Z\) splits into the dyadic component and the mutually coprime odd prime-power components. The Chinese remainder theorem makes choices of local index classes independent. Multiplying the dyadic fiber size two and each odd local root count proves the boxed fiber factorization.

**4. Local moment count.** Fix an odd \(p^a\). Exactly one discriminant \(D\bmod p^a\) is zero, with fiber size \(p^{\lfloor a/2\rfloor}\). At each \(j\) with \(0\le2j<a\), there are exactly \(\varphi(p^{a-2j})/2=(p-1)p^{a-2j-1}/2\) distinct discriminants with valuation \(2j\) and square unit; their root fibers each have size \(2p^j\). All remaining discriminants have zero root count. Because \(t\mapsto 1+8t\) is a bijection modulo odd \(p^a\), summing the \(k\)-th powers yields precisely \(C_{p,a}(k)\). Multiplication over independent target classes and the uniform dyadic factor gives the claimed all-moment formula.

For \(k=2\), the geometric sum specializes to \(\lfloor(a-1)/2\rfloor+1\), but the zero-root contribution must be combined with it: when \(a=2r\), it is \(p^{2r}=p^a\); when \(a=2r+1\), it is \(p^{2r}=p^{a-1}\). Direct substitution yields \(C_{p,a}(2)=p^a+a(p-1)p^{a-1}\) in both parity cases. An independent derivation counts pairs of roots via the invertible change \((u,v)=(x-y,x+y+1)\pmod{p^a}\): the congruence \(T(x)=T(y)\) becomes \(uv\equiv0\pmod{p^a}\), which has \(p^a+a(p-1)p^{a-1}\) ordered solutions (one case \(u=0\), and \(a\) equal contributions for the possible valuations \(0,\ldots,a-1\)). Inserting these local values proves the second-moment formula.

**5. Occupancy and both saturation conjectures.** Each attained odd-prime-power value corresponds bijectively to a square residue under \(t\mapsto1+8t\). Counting square residues by valuation gives
\[
R_{p^a}=1+\frac{p-1}{2}\sum_{j=0}^{\lfloor(a-1)/2\rfloor}p^{a-2j-1}.
\]
Evaluating this finite geometric progression gives the two parity formulas displayed above. The CRT and surjectivity of the dyadic component multiply the occupied counts, and division by \(m\) gives \(s_m\). Expanding the geometric progression yields, for odd \(a\),
\[
2R_{p^a}=1+\sum_{j=1}^{a}(-1)^{j+1}p^j;
\]
for even \(a\),
\[
2R_{p^a}=2+\sum_{j=1}^{a}(-1)^jp^j.
\]
These are the exact numerators of the two branches of Ulness's Conjecture 1. Removing \(2^\alpha\) from the saturation product proves \(s_{2^\alpha q}=s_q\) for every odd \(q\), as in Conjecture 2. No inference from finite experiments is involved.

## Verification
Run `python3 verify.py` using Python 3 and its standard library. It independently enumerates all triangular residue fibers, moments, and supports for every \(1\le m\le1000\), verifies orders \(1\le k\le6\) for \(1\le m\le299\), and checks the alternating prime-power formulas for eight odd primes through exponent seven. Successful output is preserved in `verification_output.txt`. This finite replay tests the implementation and small boundary cases; the unrestricted theorem follows from the proof above.

## Relationship to prior work
Ulness, *Structure of Triangular Numbers Modulo m* (2022), introduces the \(2m\)-cycle, residue occupancy, and multiplicity set. Theorem 5 identifies triangular residues by the square discriminant \(1+8t\); it already contains the qualitative criterion, and the present theorem does **not** claim that criterion as new. Its Conjectures 1 and 2 state the precise prime-power saturation and dyadic-factor invariance, respectively. The theorem above derives both and, beyond saturation, gives all individual full-period fibers and every integer moment for arbitrary composite moduli. The proofs rely on classical odd-prime square-root lifting and CRT; the novelty claimed is the explicit complete joint modular-distribution/moment law, not those foundational tools. The related 2019 paper on triangular lacunary trigonometric systems studies periodic sequences and Gauss-sum geometry, not these exact arithmetic fiber moments.

## Limitations
The formulas apply to complete-period fiber counts, not to a partial period with arbitrary start/end index. These are elementary finite-ring facts, not equidistribution limits. The argument does not address higher-degree figurate polynomials. Classical quadratic-residue counting is closely related and may yield equivalent formulas in other literature; bibliographic originality is relative to the inspected sources, not an assertion of global priority. Independent mathematical validation has not been performed.

## References
- D. J. Ulness, *Structure of Triangular Numbers Modulo m*, AppliedMath **2** (2022), 326–358, DOI: 10.3390/appliedmath2030020; original publication July 1, 2022; Theorems 1, 5 and Section 6 Conjectures 1–2.
- T. Vogt and D. J. Ulness, *Cornu Spirals and the Triangular Lacunary Trigonometric System*, Fractal and Fractional **3** (2019), article 40, DOI: 10.3390/fractalfract3030040.
