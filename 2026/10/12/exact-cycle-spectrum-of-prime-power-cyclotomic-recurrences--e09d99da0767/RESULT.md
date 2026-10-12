# Exact cycle spectrum of prime-power cyclotomic recurrences

## Finding

For every prime \(p\), integers \(j\ge 1\) and \(m\ge 1\), let \(d=\varphi(p^j)=p^{j-1}(p-1)\) and let \(C\) be the integral companion matrix of the monic cyclotomic polynomial \(\Phi_{p^j}(X)\). Acting on \((\mathbb Z/m\mathbb Z)^d\), the map \(C\) has **exactly** the following orbit counts. Put \(g=\gcd(p,m)\), and write \(N_r\) for the number of distinct cycles of length \(p^r\):

\[
N_0=g,\qquad
N_r=\frac{g^{p^r}-g^{p^{r-1}}}{p^r}\quad(1\le r<j),\qquad
N_j=\frac{m^d-g^{p^{j-1}}}{p^j}.
\]

All other orbit lengths occur zero times. When \(p\mid m\), one has \(g=p\), so \(N_r\) for \(r<j\) is independent of the size and other prime factors of \(m\) and equals the number of aperiodic \(p\)-symbol necklaces of length \(p^r\). For \(p\nmid m\), only one fixed point and cycles of length \(p^j\) occur. This gives a proof of the prime-index and prime-power-index cyclotomic period-count conjectures in Reference 1.

## Assumptions and scope

The recurrence is the integer linear recurrence with characteristic polynomial \(\Phi_{p^j}(X)=\sum_{k=0}^{p-1}X^{kp^{j-1}}\). A state is an ordered block of \(d\) consecutive values modulo \(m\). Its next state is given by the corresponding companion matrix; no restriction is placed on its initial block. All states are periodic because \(C^{p^j}=I\) over the integers and the constant coefficient is \(1\). The modulus \(m=1\), the prime \(p=2\), and the boundary \(j=1\) are included.

## Proof

**Step 1: module description.** Use the column companion convention, where the polynomial acts by multiplication by its indeterminate. The usual next-block update matrix for consecutive recurrence terms is the transpose of this companion matrix; since transposition preserves the integer Smith invariants of all iterated differences, the two conventions have identical modular cycle counts. The standard cyclic basis for a column companion matrix identifies the free abelian group of states with \(A=\mathbb Z[X]/(\Phi_{p^j}(X))\), where \(C\) is multiplication by \(X\). For every integer \(r\) with \(0\le r<j\), set \(Y=X^{p^r}\). The polynomial identity

\[
\Phi_{p^j}(X)=\Phi_{p^{j-r}}(X^{p^r})
\]

makes \(A\) a free module of rank \(p^r\) over \(B=\mathbb Z[Y]/(\Phi_{p^{j-r}}(Y))\). Concretely, a basis over \(B\) is \(1,X,\ldots,X^{p^r-1}\): use \(X^{p^r}=Y\) to reduce exponents, and compare the \(\mathbb Z\)-ranks \(\varphi(p^j)=p^r\varphi(p^{j-r})\) to establish independence.

**Step 2: integral Smith invariants.** In this decomposition, multiplication by \(C^{p^r}-I\) becomes the direct sum of \(p^r\) copies of multiplication by \(Y-1\) on \(B\). For each copy, its cokernel is

\[
B/(Y-1)B\cong\mathbb Z/(\Phi_{p^{j-r}}(1))\cong\mathbb Z/p\mathbb Z,
\]

since \(\Phi_{p^t}(1)=p\) for every \(t\ge1\). Over \(\mathbb Q\), multiplication by \(Y-1\) is invertible because no primitive root of unity of order \(p^t\) equals \(1\). Therefore, the Smith diagonal of \(C^{p^r}-I\) over \(\mathbb Z\) contains exactly \(p^r\) entries equal to \(p\), all others being \(1\), with no zero entries. This proves the asserted stronger integral statement, including the nontrivial Smith lemma.

**Step 3: fixed-point numbers.** Reducing the Smith form modulo \(m\), the kernel of multiplication by each Smith entry \(p\) has cardinality \(g=\gcd(p,m)\), whereas each entry \(1\) contributes one kernel element. It follows that

\[
F_r:=\#\operatorname{Fix}(C^{p^r}\bmod m)=g^{p^r}\qquad(0\le r<j).
\]

The cyclotomic identity \(X^{p^j}\equiv1\pmod{\Phi_{p^j}(X)}\) proves \(C^{p^j}=I\) and hence \(F_j=m^d\). In particular, every cycle length divides \(p^j\).

**Step 4: exact orbit counts.** By partitioning the fixed-point set of \(C^{p^r}\) according to exact period, one has \(F_r=\sum_{k=0}^r p^kN_k\). Thus \(N_0=F_0=g\), \(N_r=(F_r-F_{r-1})/p^r\) for \(1\le r\le j\). Inserting the fixed-point formulas gives precisely the displayed spectrum, with no omitted orbit lengths. For \(p\mid m\), the Möbius necklace count at length \(p^r\) is \((p^{p^r}-p^{p^{r-1}})/p^r\) for \(r\ge1\), and at length \(1\) is \(p\), proving the claimed identity. This also directly proves the divisibility of each enumerator.

## Verification

The accompanying standalone Python verifier enumerates **all** states for 102 finite parameter triples across primes \(2,3,5,7\), and compares their cycle decompositions with the exact formulas. These exhaustive tests cover 865,158 states collectively; 600 additional seeded vectors check larger parameter dimensions. All comparisons pass. For example, at \((p,j,m)=(3,2,12)\), the exact counts are 3 fixed points, 8 length-3 cycles, and 331,773 length-9 cycles. The infinite assertion is proved in the four steps above; finite enumeration cannot establish the general theorem.

Run the dependency-free verifier with `python3 verify.py`; `verification_output.txt` records its deterministic output. The verifier's file is embedded alongside this proof in the distribution.

## Relationship to prior work

Pudelko (Reference 1), Section 2 and Conjectures 1 and 3, states the corresponding total cycle counts and their necklace interpretation as conjectures, supported by computations. The proof above establishes each cycle length and multiplicity for all prime powers and all moduli, through an explicit integral Smith normal form that was not supplied in that source. It does not claim the conjectured numerical formulas themselves as newly proposed.

Baake–Neumärker–Roberts (Reference 2), Section 2.2, gives the general relation between periodic-point counts and orbit numbers for finite-lattice matrix dynamics; the method is used in Step 4. Their paper does not give the specific integral Smith forms \(\operatorname{SNF}(C^{p^r}-I)\) for prime-power cyclotomic companions, which provide the substantive fixed-point input here. Existing general Möbius inversion by itself does not establish these counts.

## Limitations

The result concerns prime-power indices only; no assertion is made for a general cyclotomic index or for Fibonacci companion matrices. The computer checks are finite corroborations, not independent proof. The identification of mathematical originality relies on the inspected literature and indexed record search; an unindexed prior equivalent could exist. Independent review has not been performed.

## References

1. Marc T. Pudelko, *Modular Periodicity of Random Initialized Recurrences*, arXiv:2510.24882 (first public version 28 October 2025), especially Section 2, Conjectures 1 and 3, https://arxiv.org/abs/2510.24882.
2. Michael Baake, Natascha Neumärker, and John A. G. Roberts, *Orbit Structure and (Reversing) Symmetries of Toral Endomorphisms on Rational Lattices*, *Discrete and Continuous Dynamical Systems* 33 (2013), 527–553, DOI: 10.3934/dcds.2013.33.527, especially Section 2.2.
3. Pieter Moree, *The formal series Witt transform*, *Discrete Mathematics* 295 (2005), 143–160, DOI: 10.1016/j.disc.2005.03.004 (background on the general necklace polynomial).
