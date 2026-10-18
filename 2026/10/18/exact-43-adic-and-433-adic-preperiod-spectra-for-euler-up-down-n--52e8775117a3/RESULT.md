# Exact 43-adic and 433-adic preperiod spectra for Euler up/down numbers

## Finding
Let \(E_n\) count alternating permutations of \(\{1,\ldots,n\}\), so that \(\sum_{n\ge0}E_n z^n/n!=\sec z+\tan z\). For each prime \(p\) and integer \(r\ge1\), define \(s(p^r)\) as the first index after which the residue sequence \((E_n\bmod p^r)\) is periodic with its least eventual period.

**Theorem.** For every integer \(r\ge1\), both \(s(43^r)\) and \(s(433^r)\) belong to \(\{r,r-1,r-2\}\). Set
\[
R_{43}=\{13,14,28,55,56,70\}\pmod{84},\qquad
R_{433}=\{1,72,144,215,216,288,360,366\}\pmod{432}.
\]
Then
\[
s(43^r)=\begin{cases}
r-2,&r=980+1806k,\ k\ge0,\\
r-1,&r\ge3,\ r\bmod84\in R_{43},\ \text{and the first case fails},\\
r,&\text{otherwise};
\end{cases}
\]
and
\[
s(433^r)=\begin{cases}
r-2,&r=71496+187056k,\ k\ge0,\\
r-1,&r\ge3,\ r\bmod432\in R_{433},\ \text{and the first case fails},\\
r,&\text{otherwise}.
\end{cases}
\]
In particular, the least exponent with \(s(433^r)=r-2\) is exactly \(71496\). The complete infinite \(43\)-adic double-defect progression gives an affirmative answer to the concrete \(43\)-adic instance of Question 5.1 of *Coprimality of consecutive Euler up/down numbers and the preperiod at odd prime powers*. It does **not** answer the question for arbitrary primes.

## Assumptions and scope
Only positive integer exponents \(r\) and the two stated odd primes are classified. The proof uses the **published** frequency expansion and the **published** prime-power preperiod criterion for Euler up/down numbers, together with a new prime-square affine-difference observation and independently checked finite residue data. The first publicly available version of the motivating research was deposited August 16, 2026. The theorem has no conditional arithmetic hypotheses and makes no assertion about preperiods at other primes.

## Proof
**1. An affine congruence at every odd prime square.** Fix any odd prime \(p\), put \(d=\operatorname{lcm}(p-1,4)\), and work in \(S=(\mathbb Z/p^2\mathbb Z)[i]\) with \(i^2=-1\). Proposition 4.4(iv) of Güleç gives the finite expansion, for all \(n\ge2\),
\[
E_n=\sum_{\substack{1\le a<p^2\\p\nmid a}}H_a(ia)^n\quad\text{in }S,
\]
where the coefficients \(H_a\) are independent of \(n\); the ordinary integers embed faithfully into \(S\). For every unit residue \(a\), Fermat's theorem and \(4\mid d\) give \((ia)^d\equiv1\pmod p\). Hence \(((ia)^d-1)^2=0\) in \(S\) modulo \(p^2\). Applying the square of the shift operator to each frequency gives
\[
E_{n+2d}-2E_{n+d}+E_n\equiv0\pmod{p^2}\qquad(n\ge2).
\]
Consequently, for all integers \(n\ge2\) and \(k\ge0\),
\[
E_{n+kd}\equiv E_n+k(E_{n+d}-E_n)\pmod{p^2}. \tag{1}
\]
Reducing (1) modulo \(p\) also shows \(E_{n+d}\equiv E_n\pmod p\) for every \(n\ge2\); the cases at indices \(0,1\) will be handled separately.

**2. From consecutive zero classes to preperiods.** Güleç's Lemmas 6.1–6.2 give the exact criterion, for each odd \(p\), \(r\ge2\), and \(1\le j\le r-1\),
\[
s(p^r)\le r-j\quad\Longleftrightarrow\quad
p^h\mid E_{r-h}\ \text{for every }1\le h\le j.\tag{2}
\]
Also \(s(p^r)\le r\) and \(s(p)=1\). Thus a defect of at least one means \(p\mid E_{r-1}\), a defect of at least two means \(p\mid E_{r-1}\) and \(p^2\mid E_{r-2}\), while a defect of at least three implies three *consecutive* terms vanish modulo \(p\).

**3. The complete \(43\)-adic table.** The exact Entringer recurrence (specified below) gives, among the indices \(2\le n\le85\), the entire set of zero classes of \(E_n\bmod43\):
\[
Z_{43}=\{12,13,27,54,55,69\}\pmod{84}.
\]
The only adjacent zero pairs are \((12,13)\) and \((54,55)\), modulo \(84\). There is no triple zero, including across the cyclic boundary. By (2), the first-defect condition is exactly \(r\bmod84\in R_{43}=Z_{43}+1\). For a double defect the only possibilities are \(r=14+84k\) or \(r=56+84k\), \(k\ge0\). The prime-square computations are
\[
E_{12}\equiv1376=43\cdot32,\quad E_{96}\equiv774\pmod{1849};
\]
\[
E_{54}\equiv774=43\cdot18,\quad E_{138}\equiv1376\pmod{1849}.
\]
By (1), \(43^2\mid E_{12+84k}\) exactly when \(32+29k\equiv0\pmod{43}\), namely \(k\equiv33\pmod{43}\); similarly, \(43^2\mid E_{54+84k}\) exactly when \(18+14k\equiv0\pmod{43}\), namely \(k\equiv11\pmod{43}\). The resulting double-defect exponents are the two residue classes \(2786\) and \(980\) modulo \(3612=43\cdot84\), whose union is \(r=980+1806k\) for \(k\ge0\). The absence of a triple zero and (2) prove all remaining branches.

**4. The complete \(433\)-adic table.** Similarly, the exact zero classes among \(2\le n\le433\) are
\[
Z_{433}=\{0,71,143,214,215,287,359,365\}\pmod{432}.
\]
Only \((214,215)\) is an adjacent pair; again there is no triple zero, including across the cyclic boundary. The first-defect residues are exactly \(R_{433}=Z_{433}+1\). A double defect requires \(r=216+432k\) for some \(k\ge0\). Exact reduction modulo \(433^2=187489\) gives
\[
E_{214}\equiv38104=433\cdot88,\qquad
E_{646}\equiv175365\pmod{187489}.
\]
Their difference modulo \(433^2\) is \(433\cdot317\). By (1), \(433^2\mid E_{214+432k}\) precisely when
\[
88+317k\equiv0\pmod{433},
\]
whose unique solution is \(k\equiv165\pmod{433}\). Therefore the **entire infinite** double-defect set is
\[
r=216+432(165+433j)=71496+187056j,\qquad j\ge0.
\]
The zero classes and criterion (2) exclude any defect of three or more. For \(r=1,2\), \(E_0=E_1=1\) and (2) or the initial preperiod bound give \(s(p)=1\), \(s(p^2)=2\). This completes every branch of the theorem.

## Verification
The file `verify.py` runs two structurally different exact modular recurrences: the Entringer triangle and the quadratic convolution for \(\sec z+\tan z\), namely \(2E_{n+1}=\sum_{k=0}^{n}\binom{n}{k}E_kE_{n-k}+\mathbf 1_{n=0}\). It checks their agreement at every index through \(3d+9\), exhausts every first-prime zero class, checks the prime-square second difference on all available indices, and certifies the stated prime-square residues and unique affine roots. Run `python3 verify.py`; the expected last line is `CERTIFICATE_OK`.

The finite computation is not being used as an infinite proof. The infinity step is (1), proved from the published frequency expansion; the exhaustive zero sets together with (2) then establish the exact formulas for every exponent.

## Relationship to prior work
Güleç, *Modular periodicity of the Euler up/down numbers at odd prime powers* (first publicly deposited August 16, 2026; arXiv:2608.27058), proves the exact eventual periods and preperiod divisibility criterion, but does not give the affine prime-square formula here or the full \(43\)- and \(433\)-adic phase diagrams. His published numerical example \(s(43^{980})=978\) is retained, not claimed as new.

*Coprimality of consecutive Euler up/down numbers and the preperiod at odd prime powers* (2026) proves a finite census for exponents up to \(10001\), and reports a measurement through \(20001\). Its Question 5.1 explicitly asks whether the \(43\)-adic progression continues indefinitely and notes the difficulty of the half-period \(1806\). It also lists \(433\) among primes dividing two consecutive Euler numbers but gives no double-defect exponent at that prime. The present theorem proves the concrete progression for all exponents and supplies the first complete \(433\)-adic spectrum and its sharp initial exponent \(71496>20001\). Ramassamy (2017) formulated the earlier general period/preperiod questions.

## Limitations
This is a two-prime classification, not a proof of the proposed universal bound \(s(p^r)\ge r-2\) for all primes. The general prime-square affine congruence follows from a published expansion rather than a new self-contained construction of its coefficients. The finite certificates rely only on exact modular arithmetic; their independent recomputation here does not amount to a separate external audit. A prior unindexed classification for the stated primes remains a residual originality risk.

## References
1. B. Güleç, *Modular periodicity of the Euler up/down numbers at odd prime powers*, arXiv:2608.27058, primary MSC 11B50 (2026). First public version: Zenodo, August 16, 2026, doi:10.5281/zenodo.21960727.
2. *Coprimality of consecutive Euler up/down numbers and the preperiod at odd prime powers*, Ideosphere, PDF https://ideosphere.ai/papers/updown-preperiod-v1.pdf (2026), in particular Theorem 4.2, Remark 5.2 and Question 5.1.
3. S. Ramassamy, *Modular periodicity of the Euler numbers and a sequence by Arnold*, arXiv:1712.08666 (2017).
