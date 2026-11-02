# Prime-power separation spectrum for two-block conjugate words in permutation automata

## Finding

For positive integers \(a,b\), consider the binary words \(u=0^a1^b\) and \(v=1^b0^a\). Let \(s(a,b)\) be the smallest positive integer \(m\) for which a complete deterministic finite automaton on \(m\) states, with both letter transitions permutations, accepts exactly one of \(u,v\). Write \(L_m=\operatorname{lcm}(1,2,\ldots,m)\).

**Theorem.** A separating permutation automaton with exactly \(m\) states exists if and only if the following corresponding condition holds:

- \(m\le2\): never;
- \(m=3\): \(6\nmid a\), \(6\nmid b\), and at least one of \(a,b\) is odd;
- \(m=4\): \(12\nmid a\), \(12\nmid b\), and not both \(a,b\) are divisible by \(6\);
- \(m\ge5\): \(L_m\nmid a\) and \(L_m\nmid b\).

In particular, the set of achievable values of \(s(a,b)\), over all positive \(a,b\), is precisely the set of prime powers at least \(3\). The shortest possible total word length \(a+b\) realizing a given achievable minimum state count \(q\) is

\[
\mu(q)=\begin{cases}
2,&q=3,\\
4,&q=4,\\
12,&q=5,\\
L_{q-1}+1,&q\ge7\text{ a prime power}.
\end{cases}
\]

For \(q\ge7\), exactly the exponent pairs \((L_{q-1},1)\) and \((1,L_{q-1})\) attain that minimum. For \(q=3,4,5\), the corresponding unique unordered minimizing pairs are \((1,1)\), \((2,2)\), and \((6,6)\), respectively.

## Assumptions and scope

An automaton has a finite state set \(Q\), initial state \(q_0\), accepting set \(F\subseteq Q\), and two total transition functions \(A,B:Q\to Q\), each bijective. All states, including unreachable ones, count toward \(|Q|\). There is no promise that the automaton is minimal or that \(q_0\) is reachable from every state. The words \(u,v\) are evaluated from the same initial state; a separating automaton must accept exactly one. The empty word is excluded by \(a,b\ge1\). The cases \(m=1,2\) are part of the theorem.

The state count is *permutation-automaton* separation complexity, not general deterministic-automaton separation complexity. No claim is made about transformations that are not bijections.

## Proof

**1. Reduction to a positive identity in a symmetric group.** Every pair \(A,B\in S_m\) gives the respective word transformations \(A^aB^b\) and \(B^bA^a\), with the particular function-composition convention immaterial to their equality. If these transformations differ, some state has different images; choose that state as initial and choose an accepting set containing exactly one image. Conversely, if the transformations always agree, no starting state and accepting set can distinguish the words. Consequently, degree \(m\) separates exactly when

\[
\exists A,B\in S_m:\quad A^aB^b\ne B^bA^a. \tag{1}
\]

**2. Normal closure criterion.** For \(t\ge1\), set \(H_t=\langle g^t:g\in S_m\rangle\). Conjugation permutes the generators, so \(H_t\) is normal. The positive identity \(X^aY^b=Y^bX^a\) holds in \(S_m\) if and only if \(H_a\) centralizes \(H_b\) *elementwise*. Indeed, if every single \(a\)-th power commutes with every single \(b\)-th power, then the corresponding generated groups commute, and the converse is immediate. Moreover,

\[
H_t=1\quad\Longleftrightarrow\quad L_m\mid t,\tag{2}
\]

because the order of a permutation is the least common multiple of its cycle lengths, the exponent of \(S_m\) is \(L_m\), and each cycle length from \(1\) through \(m\) occurs.

**3. Degrees at least five.** For \(m\ge5\), the only normal subgroups of \(S_m\) are \(1,A_m,S_m\). Every nontrivial normal subgroup therefore contains the nonabelian subgroup \(A_m\), so two nontrivial normal subgroups cannot centralize one another elementwise. By (1) and (2), degree \(m\) separates precisely when neither exponent is divisible by \(L_m\).

**4. The exceptional small degrees.** For \(m=3\), the power-generated normal subgroup is \(1\) if \(6\mid t\), \(A_3\) if \(t\) is even and \(3\nmid t\), and \(S_3\) if \(t\) is odd. The sole pair of nontrivial power-generated groups that centralize each other is \((A_3,A_3)\), because \(A_3\) is cyclic and \(S_3\) is nonabelian. The stated degree-three criterion follows. For \(m=4\), the possibilities are \(1\) if \(12\mid t\), the Klein four group \(V_4\) if \(t\equiv6\pmod{12}\), \(A_4\) if \(t\) is even and \(3\nmid t\), and \(S_4\) if \(t\) is odd. These are exhaustive (in the second case, even multiples of three not divisible by four are exactly residue six modulo twelve). Apart from the trivial subgroup, only \(V_4\) and itself centralize one another elementwise; \(V_4\) is abelian but is not elementwise centralized by \(A_4\). This gives the degree-four criterion. For \(m\le2\), \(S_m\) is abelian and cannot separate.

**5. Attainable least degrees.** The separating property is monotone in \(m\): add unused fixed states to an existing automaton. Above degree five, the criterion in Step 3 changes between consecutive degrees only if \(L_m>L_{m-1}\). This occurs precisely when \(m\) is a prime power. Hence no degree \(m\ge6\) other than a prime power can be the *least* separating degree. The pairs \((a,b)=(1,1),(2,2),(6,6)\) have respective least degrees \(3,4,5\) by the three criteria. For any prime power \(q\ge7\), set \((a,b)=(L_{q-1},1)\). All degrees below \(q\) fail, because \(a\) is divisible by their respective symmetric-group exponents. But \(L_q>L_{q-1}\), so degree \(q\) separates. Thus every prime power \(q\ge3\) occurs and nothing else does.

**6. Exact minimum word length.** The three exceptional possibilities are checked from the small-degree criteria: at least two letters are necessary and \((1,1)\) attains degree three; to exclude degree three while permitting four, both positive exponents must be even, or one must be divisible by six; the least sum is four, uniquely \((2,2)\). To exclude degree four while permitting degree five, either an exponent is divisible by twelve (then the sum is at least thirteen), or both exponents are divisible by six (then the sum is at least twelve); the unique sum-twelve solution is \((6,6)\). For a prime power \(q\ge7\), an exponent must be divisible by \(L_{q-1}\), since otherwise the degree \(q-1\) criterion would already separate. Thus \(a+b\ge L_{q-1}+1\), and equality requires \((a,b)=(L_{q-1},1)\) or its exchange. Both attain least degree \(q\) by Step 5. This completes the proof.

## Verification

The standalone `check.py` enumerates the complete symmetric group in degrees two through six. For each degree, it constructs the power image sets and their centralizers for *all* exponent residue pairs modulo \(L_m\) and compares the computed separating/nonseparating result with the theorem. The numbers of checked ordered residue pairs in degrees \(2,3,4,5,6\) are respectively \(4,36,144,3600,3600\). Additional checks evaluate \(10{,}000\) positive exponent pairs up to \(100\) against the predicted achievable least-degree spectrum; test least-degree witnesses through prime power \(37\); and directly confirm concrete noncommuting permutation witnesses for degrees \(3,4,5,7,8,9,11\). Run `python3 check.py`; the corresponding recorded output is `check_output.txt`.

These finite tests are independent consistency checks, **not** a substitute for the normal-subgroup proof for arbitrarily large degrees and exponents. The proof uses standard elementary finite-group structure and does not require an external computation or unproved numerical conjecture.

## Relationship to prior work

Bulatov, Karpova, Shur and Startsev (2017), Section 3, explicitly record the previously known \(S_3\) identity \(X^2Y^2=Y^2X^2\); that particular degree-four example is **not claimed to be new**. They give general lower bounds, shortest small-degree positive identities, and in Proposition 15 an identity involving powers of \(XY\) and \(YX\). Their statements do not supply the full two-parameter identity criterion for the *different* words \(X^aY^b\) and \(Y^bX^a\), nor the corresponding prime-power least-degree spectrum and sharp minimum lengths. Demaine, Eisenstat, Shallit and Wilson (2011), in their section on permutation automata, analyze word separation and group identities for general word pairs rather than this exact two-block rotation. Xu and Regan (2026), publicly submitted October 8, study asymptotic worst-case separation and positive identities, which motivates isolating an exactly solvable conjugate pair family. The complete 2026 manuscript was not accessible for comparison, so priority relative to its uninspected portions is not certified. The related older literature on group identities is acknowledged, and no novelty is claimed for symmetric-group normal subgroup classification itself.

## Limitations

The result treats exactly two nonempty constant-symbol blocks, their order exchange, and automata whose *both* transitions are permutations. It does not determine unrestricted deterministic-automaton separation, rotations with three or more blocks, arbitrary positive words, or asymptotic worst-case separation. The normal-subgroup argument is mathematical; the finite checks cover only their stated dimensions. Literature-priority assessment remains non-exhaustive because one especially recent plausible manuscript and some older references could not be inspected in full. Mathematical validity and independent priority review have not undergone an external audit.

## References

1. Chen Xu and Kenneth Regan, *An Improved Lower Bound for Separating Words by Permutation Automata*, arXiv:2610.11098, first submitted October 8, 2026. https://arxiv.org/abs/2610.11098
2. Andrei A. Bulatov, Olga Karpova, Arseny M. Shur and Konstantin Startsev, *Lower Bounds on Words Separation: Are There Short Identities in Transformation Semigroups?*, Electronic Journal of Combinatorics 24(3) (2017), P3.35. DOI:10.37236/6450. https://www.combinatorics.org/ojs/index.php/eljc/article/download/v24i3p35/pdf/
3. Erik D. Demaine, Sarah Eisenstat, Jeffrey Shallit and David A. Wilson, *Remarks on Separating Words*, 2011. https://erikdemaine.org/papers/WordSep_DFCS2011/paper.pdf
4. J. M. Robson, *Separating Words with Machines and Groups*, RAIRO Theoretical Informatics and Applications 30 (1996), 81–86. https://www.numdam.org/item/ITA_1996__30_1_81_0/
5. P. V. Gimadeev and M. N. Vyalyi, *Identical Relations in Symmetric Groups and Separating Words with Reversible Automata*, 2010, DOI:10.1007/978-3-642-13182-0_14 (metadata inspected; full text not available).
