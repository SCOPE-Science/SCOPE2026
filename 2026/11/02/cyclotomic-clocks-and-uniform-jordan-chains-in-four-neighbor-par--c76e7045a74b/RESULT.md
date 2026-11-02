# Cyclotomic clocks and uniform Jordan chains in four-neighbor parity tori

## Finding

For integers \(a\ge2\), \(b\ge0\), and odd \(m\ge3\), consider the periodic grid \(C_M\square C_N\) of dimensions \(M=2^a\) and \(N=m2^b\). Let \(q\) be a power of two and let \(T\) act on \(\mathbb F_q^{MN}\) by replacing each cell with the sum of its four distinct nearest neighbors. Define \(d=2^b\), \(P=M/2\), \(L=\max(M,d)/2\), \(c=2\min(M,d)\), and \(H=\max(P,d)\). For the set \(\mu_m\) of \(m\)-th roots of unity in an algebraic closure, the complete Jordan form over that closure is

\[
 T\sim J_L(0)^{\oplus c}\ \oplus\!
 \bigoplus_{\zeta\in\mu_m\setminus\{1\}}
 J_H(\zeta+\zeta^{-1})^{\oplus 2\min(P,d)}.
\]

Repeated eigenvalues are deliberately listed repeatedly, once for each root \(\zeta\); thus both \(\zeta\) and \(\zeta^{-1}\) contribute. The zero-primary dimension is \(Md\), while the invertible-primary dimension is \(Md(m-1)\). In particular, every configuration becomes periodic after at most \(L\) steps, and this bound is sharp.

The Jordan form yields an exact temporal orbit census without factoring a large matrix. For positive integer \(t=2^j u\), \(u\) odd, define

\[
 B_m(u)=\deg\gcd_{\mathbb F_2[Y]}\left(
 1+Y+\cdots+Y^{m-1},\ (Y+1)^{2u}+Y^u\right)
\]

and

\[
 R(t)=2\min(P,d)\min(H,2^j)B_m(u).
\]

Then the total number of configurations fixed by \(T^t\) is exactly \(q^{R(t)}\). If \(A(p)\) denotes the number of configurations of *least* positive temporal period \(p\), then

\[
 A(p)=\sum_{r\mid p}\mu(p/r)q^{R(r)},\qquad
 \#\{\hbox{primitive period-}\!p\hbox{ orbits}\}=\frac{A(p)}p.
\]

Here \(\mu\) is the classical Möbius function. The number of configurations with *first periodic-entry time* exactly \(s\) and eventual least period \(p\) is

\[
 A(p)\times\begin{cases}
 1,&s=0,\\
 q^{c\min(s,L)}-q^{c\min(s-1,L)},&1\le s\le L,\\
 0,&s>L.
 \end{cases}
\]

All populations refer to labelled cells and temporal orbits; spatial rotations are **not** identified.

There are two simple arithmetic thresholds: nonzero fixed configurations exist if and only if \(3\mid m\), whereas genuine primitive three-cycles exist if and only if \(5\mid m\). If \(m=5\), for example, the system on \(C_4\square C_5\) over \(\mathbb F_2\) has exactly one fixed configuration, \(85\) primitive three-cycles, and \(10880\) primitive six-cycles, and no other primitive periodic orbits. Its exact maximum transient is two updates.

Writing \(E_m\) for the least positive odd integer \(e\) such that \(B_m(e)=m-1\), the largest attainable least period (equivalently the order of the update restricted to its periodic subspace) is exactly \(E_mH\). Such an \(E_m\) exists because every nonzero element of an algebraic closure of \(\mathbb F_2\) has finite odd multiplicative order.

## Assumptions and scope

The four-neighbor rule excludes the center and includes the two horizontal and two vertical nearest neighbors, each counted once. The restrictions \(M\ge4\) and \(N\ge3\) ensure that these are distinct cells. The field may be any finite field of characteristic two. No assertion is made for grids whose first circumference is not a power of two, nor for nonlinear rules, boundary grids, or other neighborhood kernels. The word “periodic” refers to the time evolution of the finite-dimensional vector configuration, not to the spatial periodic boundary condition.

## Proof

**1. Algebraic model.** Identify configurations with the group algebra

\[
 \mathcal R=\mathbb F_q[X^{\pm1},Y^{\pm1}]/(X^M-1,Y^{md}-1),
\]

where the update is multiplication by \(h=X+X^{-1}+Y+Y^{-1}\). Extending scalars to an algebraic closure does not change ranks or kernel dimensions. In characteristic two,

\[
 X^M-1=(X+1)^M,\qquad
 Y^{md}-1=(Y^m-1)^d.
\]

Since \(m\) is odd, \(Y^m-1\) has \(m\) distinct roots. Chinese remaindering thus gives one \(Y\)-local factor of length \(d\) for each \(\zeta\in\mu_m\), tensored with the \(X\)-local algebra of length \(M\).

**2. Local Jordan modules.** For \(X\) near one, the identity

\[
 X+X^{-1}=X^{-1}(X+1)^2
\]

shows that multiplication by \(X+X^{-1}\) has two zero-Jordan blocks, each of size \(P=M/2\): its powers have the same kernels as multiplication by \((X+1)^2\). Likewise,

\[
 Y+Y^{-1}-(\zeta+\zeta^{-1})
 =Y^{-1}(Y-\zeta)(Y-\zeta^{-1}).
\]

At \(\zeta\ne1\), the roots \(\zeta\) and \(\zeta^{-1}\) are distinct, so the factor \(Y-\zeta^{-1}\) is a unit in the local algebra at \(\zeta\). Consequently the shifted multiplier has exactly one nilpotent block of length \(d\). At \(\zeta=1\), it has one zero-Jordan block of length one when \(d=1\), and two blocks of length \(d/2\) when \(d\ge2\).

**3. Power-of-two tensor lemma.** If \(r\) and \(s\) are powers of two, the Kronecker sum \(J_r(0)\otimes I_s+I_r\otimes J_s(0)\) is a direct sum of \(\min(r,s)\) blocks \(J_{\max(r,s)}(0)\). Indeed, in the algebra \(K[u,v]/(u^r,v^s)\), the sum acts as multiplication by \(u+v\). Assuming \(r\ge s\), the invertible linear coordinate change \(w=u+v\) transforms the relations into \(w^r=v^s=0\), since \((w+v)^r=w^r+v^r\) and \(v^r=0\). The \(s\) independent \(v\)-monomials each generate a \(w\)-chain of length \(r\).

Apply the lemma to the two \(X\) blocks and the one (or two) \(Y\) blocks. At \(\zeta=1\), the result is exactly \(c\) blocks of length \(L\), both for \(d=1\) and for \(d\ge2\). At each \(\zeta\ne1\), it is \(2\min(P,d)\) blocks of length \(H\), all shifted to eigenvalue \(\zeta+\zeta^{-1}\). This proves the Jordan decomposition, including all boundary cases and multiplicities. None of these latter eigenvalues is zero, because \(\zeta+\zeta^{-1}=0\) in characteristic two implies \(\zeta^2=1\), hence \(\zeta=1\).

**4. Periodic fixed points and exact temporal populations.** The nilpotent primary part contributes only zero to \(\ker(T^t-I)\). A nonzero Jordan block \(J_H(\lambda)\), with \(\lambda\) of odd order, contributes a kernel of dimension \(\min(H,2^j)\) to \(J_H(\lambda)^t-I\) precisely when \(\lambda^u=1\), and contributes nothing otherwise. The first assertion follows because \((\lambda I+N)^u-I\) has a simple factor in \(N\) when \(\lambda^u=1\) and \(u\) is odd, and raising it to the \(2^j\)-th power raises the zero multiplicity to \(2^j\). The condition \((\zeta+\zeta^{-1})^u=1\) is equivalent, after multiplication by \(\zeta^u\), to \((\zeta+1)^{2u}+\zeta^u=0\). The \(m\)-th roots other than one are the simple roots of \(1+Y+\cdots+Y^{m-1}\), so their number satisfying this condition is \(B_m(u)\). Sum the block kernel dimensions to obtain \(R(t)\), and raise \(q\) to this dimension to count solutions. Möbius inversion counts exact periods; division by \(p\) counts temporal orbits.

The Fitting decomposition separates each configuration uniquely into a nilpotent part and an invertible periodic part. The number of nilpotent configurations extinguished by time \(s\) is \(q^{c\min(s,L)}\), which gives the exact entry shells and their products with the period counts. A vector whose nilpotent component begins a length-\(L\) Jordan chain witnesses the sharp transient. Similarly, a cyclic vector in every invertible eigen-primary component attains the least common multiple of all their odd eigenvalue orders times \(H\), giving \(E_mH\).

**5. Low-period arithmetic thresholds.** At \(u=1\) the root condition polynomial is \(Y^2+Y+1\), whose roots have multiplicative order three. At \(u=3\), it factors as

\[
 (Y^2+Y+1)(Y^4+Y^3+Y^2+Y+1).
\]

The second factor has exactly the primitive fifth roots. The nonzero fixed and primitive-three-cycle assertions follow by comparing \(R(1)\) and \(R(3)\). In the \(m=5\), \(M=4\), \(d=1\) example, \(R(1)=0\), \(R(3)=8\), and \(R(6)=16\). Thus the numbers of primitive orbits are \((2^8-1)/3=85\) and \((2^{16}-2^8)/6=10880\).

## Verification

A standalone standard-library Python script, `verify_torus.py`, constructs the actual binary adjacency matrices, computes their powers, and compares direct Gaussian-elimination nullities of both \(T^t\) and \(T^t-I\) against the two formulas. The script tests sixteen dimension triples, including odd parts \(3,5,7,9,11\), and fourteen times for each: \(224\) separate paired rank and fixed-point tests. It additionally enumerates all \(4096\) binary states on the \(4\times3\) torus and checks their joint first-entry/least-period populations against Möbius inversion. Run `python verify_torus.py` from the folder containing the file. The included `verification_output.txt` records the successful replay. These finite checks support the stated algebraic proof and do not purport to prove the infinite family by enumeration.

## Relationship to prior work

Cordovil, Dilão, and Noronha da Costa (1986) established general temporal-period counting for one-dimensional infinite additive cellular automata, not the present finite two-dimensional toric Jordan decomposition. Zaidenberg (2006, two papers) developed harmonic-character, spectrum, Fourier, and convolution methods on lattices and periodic tori; the group-algebra framework and semisimple spectral reduction are classical antecedents. The proof here obtains *all elementary Jordan block lengths* for the particular four-neighbor kernel with a dyadic circumference, then deduces the entire temporal orbit and first-entry census, including an explicit polynomial-gcd clock. The general semisimple spectral statements alone do not determine nilpotent chain lengths or the transient and temporal orbit counts. An earlier zero-primary-only result for this torus family supplies the first-entry law but not its nonzero-primary Jordan blocks, root-order census, or primitive periods. Comparison of exact implications is essential; absence of a matching title is not offered as a novelty proof.

## Limitations

The first circumference must be a power of two. The clock \(E_m\) is defined algorithmically by finite-field roots (or an equivalent polynomial gcd), rather than by a uniform elementary integer formula for every odd \(m\). The result makes no claim about spatially quotienting orbits or the dynamics under other update neighborhoods. Historical equivalence through differently phrased or unindexed group-algebra literature remains possible. Computational verification is finite, and no independent external audit has been performed.

## References

1. R. Cordovil, R. Dilão, A. Noronha da Costa, *Periodic Orbits for Additive Cellular Automata*, Discrete & Computational Geometry **1** (1986), 277–288. DOI: `10.1007/BF02187700`.
2. M. Zaidenberg, *Convolution Equations on Lattices: Periodic Solutions with Values in a Prime Characteristic Field*, arXiv:`math-ph/0606070`, originally posted 2006-06-29.
3. M. Zaidenberg, *Periodic Binary Harmonic Functions on Lattices*, arXiv:`math-ph/0608027`, originally posted 2006-08-10.
