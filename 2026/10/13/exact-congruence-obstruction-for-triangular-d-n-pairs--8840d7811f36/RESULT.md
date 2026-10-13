# Exact congruence obstruction for triangular \(D(n)\) pairs
## Finding
For every positive integer \(n\), the congruence \(T_aT_b+n\equiv c^2\pmod M\), with \(T_j=j(j+1)/2\), has integer solutions \((a,b,c)\) for every positive modulus \(M\) if and only if \(n\not\equiv2,5\pmod 9\).

Thus the two residue classes excluded by the known modulo-\(9\) argument are not merely necessary obstructions: they are the complete set of congruence obstructions. In particular, values such as \(n=12,17,42\), which have been highlighted because no small integral triangular \(D(n)\)-pair is apparent, nevertheless satisfy the defining equation modulo every positive modulus.

## Assumptions and scope
Write \(T_j=j(j+1)/2\) for the \(j\)-th triangular number. The statement concerns congruence solvability only. It does not assert the existence of an integral solution to \(T_aT_b+n=c^2\), nor does it assert a Hasse principle for that affine equation.

It is enough to solve the congruence modulo every prime power. For odd prime powers, the residue class of an index determines its triangular number. At the prime \(2\), an index is tracked one power more finely when the Chinese remainder theorem is applied, because \(T_j\bmod 2^k\) has period dividing \(2^{k+1}\).

## Proof
First suppose \(n\equiv2\pmod3\). Modulo \(3\), triangular numbers are \(0\) or \(1\), and squares are \(0\) or \(1\). Hence a solution forces \(T_a\equiv T_b\equiv1\pmod3\) and \(c\equiv0\pmod3\). The congruence \(T_j\equiv1\pmod3\) forces \(j\equiv1\pmod3\), and then in fact \(T_j\equiv1\pmod9\). Therefore modulo \(9\) one must have \(1+n\equiv0\pmod9\), i.e. \(n\equiv8\pmod9\). Consequently \(n\equiv2\) or \(5\pmod9\) is impossible.

Now assume \(n\not\equiv2,5\pmod9\).

For powers of \(2\), the map
\[
j\longmapsto T_j\pmod{2^k},\qquad 0\le j<2^k,
\]
is a bijection. Indeed, if \(T_a\equiv T_b\pmod{2^k}\), then \((a-b)(a+b+1)\) is divisible by \(2^{k+1}\). The two factors have opposite parity. In the indicated range the even factor cannot be \(a+b+1\), because \(1\le a+b+1<2^{k+1}\); hence \(2^{k+1}\mid a-b\), so \(a=b\). Thus every residue occurs. Choose \(T_a\equiv4-n\pmod{2^k}\), set \(b=1\), and set \(c=2\).

Let \(p>3\) be prime. Put
\[
f(t,x,y)=x^2-t(t+1)y^2+t(t+1)-16n.
\]
Choose \(t\in\mathbb F_p\setminus\{0,-1\}\) with \(t(t+1)\ne16n\). Such a choice exists because the excluded quadratic equation has at most two roots. For \(d=t(t+1)\) and \(r=16n-d\), the equation
\[
x^2-dy^2=r
\]
has a solution over \(\mathbb F_p\): the two sets of residues \(\{x^2\}\) and \(\{r+dy^2\}\) each have \((p+1)/2\) elements, so they intersect. Because \(r\ne0\), the resulting \((x,y)\) is not \((0,0)\). Hence at least one of \(2x\) and \(-2dy\) is nonzero modulo \(p\), and the solution lifts by Hensel's lemma to every \(p^k\). Taking \(a=t\), \(x=4c\), and \(y=2b+1\) recovers
\[
T_aT_b+n=c^2.
\]

It remains to treat powers of \(3\).

If \(n\equiv0\pmod3\), fix \(b=1\) and \(c=0\). The polynomial \(F(a)=a(a+1)+2n\) has \(F(0)\equiv0\pmod3\) and \(F'(0)=1\), so Hensel's lemma gives \(T_a+n\equiv0\pmod{3^k}\) for every \(k\).

If \(n\equiv1\pmod3\), fix \(a=0\). The polynomial \(c^2-n\) has the simple root \(c\equiv1\pmod3\), so \(n\) is a square modulo every \(3^k\).

The only remaining admissible class is \(n\equiv8\pmod9\). Write \(n=8+9m\), and set
\[
a=1+3u,\qquad b=1+3v,\qquad c=3w.
\]
The exact identity
\[
T_{1+3u}=1+9T_u
\]
reduces the equation to
\[
w^2=1+m+T_u+T_v+9T_uT_v.
\]
Modulo \(3\), choose \((u,v)\equiv(0,0),(1,1),(1,0)\) according as \(m\equiv0,1,2\pmod3\), and choose \(w\equiv1\pmod3\). This gives a root. After multiplying by \(4\), the defining polynomial has derivative \(8w\), which is a unit modulo \(3\); Hensel's lemma therefore lifts the root to every \(3^k\).

For a general modulus \(M\), choose the preceding solutions for each prime-power divisor of \(M\) and combine the coordinates by the Chinese remainder theorem. At the \(2\)-part, combine the index coordinates modulo one additional power of \(2\), which preserves the required triangular residues. This gives a simultaneous solution modulo \(M\), completing the proof.

## Verification
The supplied verifier checks three finite shadows of the proof: bijectivity of triangular residues modulo \(2^k\) for \(1\le k\le8\); the exact obstruction pattern modulo \(3^k\) for \(1\le k\le5\); and existence of nonsingular odd-prime seeds for each residue class modulo the primes \(5,7,11,13,17,19\). It also checks the identity \(T_{1+3u}=1+9T_u\) on a symmetric finite range.

These computations are corroborative only. The theorem for all moduli follows from the symbolic arguments above, not from finite enumeration.

## Relationship to prior work
Bagchi and Zhou-Zheng prove that triangular \(D(n)\)-pairs cannot exist for \(n\equiv2,5\pmod9\), and they prove congruence solvability for moduli not divisible by \(9\), together with prime-power lifting away from \(3\). Their discussion isolates the prime \(3\) as the missing local case. The present result supplies that missing \(3\)-adic analysis and turns the necessary modulo-\(9\) condition into an exact all-modulus classification.

Bliznac Trebješanin studies actual triangular \(D(a)\)-pairs and triples and obtains necessary conditions and infinite families. Radić studies selected \(D(u^2)\)-triples and quadruples. Those results concern integral pairs or larger tuples rather than solvability of the pair equation modulo every modulus.

## Limitations
The result is purely local. It does not decide whether an admissible \(n\) possesses an integral triangular \(D(n)\)-pair, and it does not explain failures of integral solvability for admissible values. The proof uses only elementary finite-field counting, Hensel lifting, and the Chinese remainder theorem.

## References
1. S. Bagchi and C. Zhou-Zheng, *Diophantine m-tuples of Triangular Numbers*, arXiv:2608.27697v1, 2026.
2. M. Bliznac Trebješanin, *On Diophantine pairs and triples of triangular numbers*, arXiv:2603.29565, 2026.
3. P. Radić, *On some \(D(u^2)\)-triples and quadruples of triangular numbers*, arXiv:2609.28018v1, 2026.
