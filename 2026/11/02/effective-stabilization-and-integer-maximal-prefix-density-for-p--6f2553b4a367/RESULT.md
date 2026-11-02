# Effective stabilization and integer maximal-prefix density for periodic palindrome-rich words

## Finding

Let \(w=v^{\omega}\) be a nonconstant purely periodic right-infinite word over a finite alphabet, with **least** period \(p\ge2\), and suppose infinitely many prefixes of \(w\) are palindromes. Put \(L(n)=\operatorname{PL}(w[1,n])\), where \(\operatorname{PL}\) is the minimum number of nonempty palindromes concatenating to a given nonempty word. Then

\[
 1\le L(n)\le p\quad(n\ge1),\qquad L(n+p)=L(n)\quad(n\ge p(p-1)+1).
\]

The least period and the quadratic cutoff are effective: **the entire eventual profile is obtained by computing the finitely many values up through \(p^2+1\)**. Let \(M=\max_{n\ge1}L(n)\), and define

\[
 t=\#\{j\in\{p(p-1)+1,\ldots,p^2\}:L(j)=M\}.
\]

For \(P_w(N)=\#\{1\le j\le N:w[1,j]\text{ is a palindrome}\}\), and \(T_w(N)=\{1\le j\le N:L(j)=\max_{1\le i\le j}L(i)\}\) (including ties), the ordinary limit exists and is a strictly bounded **integer**:

\[
 \lim_{N\to\infty}\frac{|T_w(N)|}{P_w(N)}=t,\qquad 1\le t\le p-1.
\]

The upper bound is sharp at every least period \(p\ge2\): for different letters \(a,b\) and any \(r,s\ge1\) with \(r+s=p\), the word \(w=(a^rb^s)^\omega\) has \(t=p-1\). At period two it also attains the lower bound \(t=1\).

## Assumptions and scope

Indices start at one and all palindromic factors in a factorization are nonempty. The period \(p\) is **primitive** (the smallest possible), not merely any advertised block length. Infinitely many palindromic prefixes are essential: without this assumption no fixed reflection symmetry need exist. The empty prefix is excluded from both counting functions. The definition of \(T_w\) counts a tie with an earlier maximum, not only a strict new record. No ergodic, stochastic, or alphabet-size condition beyond finiteness is used.

## Proof

**1. Global reflection and long palindromes.** Let \(q\ge p\) be the length of one palindromic prefix. Extend \(w\) periodically in both directions. Palindromicity on \([1,q]\) includes all residue classes modulo \(p\), so by periodicity

\[
 w_i=w_{q+1-i}\qquad(i\in\mathbb Z).
\]

A factor \(w[i,j]\) of length at least \(p\) is a palindrome only if its reflection about endpoint sum \(i+j\) is likewise a symmetry of the two-sided periodic word. Composing it with the fixed reflection supplies period \(i+j-(q+1)\); minimality of \(p\) forces

\[
 i+j\equiv q+1\pmod p.
\]

Conversely this congruence makes \(w[i,j]\) a palindrome, regardless of length, by the global reflection and periodicity. Thus a palindrome factor of length at least \(p\) can be lengthened by \(p\) on its right, and any palindrome factor of length at least \(p+1\) can be shortened by \(p\) on its right, with the resulting nonempty factor still a palindrome. Later factors can be translated by \(p\) without changing their letters.

Applied to prefixes, this also proves directly that there is exactly one residue class \(q\pmod p\) of palindromic-prefix lengths \(n\ge p\). This periodic-prefix assertion is already recorded in Fischler's Lemma 5.6 and is not claimed as new.

**2. Uniform bound on palindromic length.** For every \(n\ge p\), choose the unique integer \(k\in\{0,\ldots,p-1\}\) with \(k+n\equiv q\pmod p\). The suffix \(w[k+1,n]\) is a palindrome, while its preceding \(k\) symbols may each form a singleton palindrome. Therefore \(L(n)\le k+1\le p\). For \(n<p\), the bound \(L(n)\le n<p\) is immediate.

**3. Explicit stabilization.** Fix \(n>p(p-1)\), and let an optimal palindrome factorization of \(w[1,n]\) contain \(k\le p\) factors. Since \(n>p(p-1)\), at least one factor has length at least \(p\). Lengthen that factor by \(p\), and translate all following factors by \(p\). Step 1 makes a factorization of \(w[1,n+p]\) into the same \(k\) palindrome factors, so \(L(n+p)\le L(n)\). Conversely, an optimal factorization of \(w[1,n+p]\) has at most \(p\) factors; since \(n+p>p^2\), one factor has length at least \(p+1\). Shorten it by \(p\) and translate the following factors back by \(p\). This proves \(L(n)\le L(n+p)\). Together these inequalities give equality for every integer \(n\ge p(p-1)+1\). The values for one complete period from \(p(p-1)+1\) to \(p^2\) can therefore be read from the first \(p^2\) entries (the additional value at \(p^2+1\) permits an immediate boundary check).

**4. The running maximum and the density limit.** A published translation lemma (Rukavicka, Lemma 6.1) states that if \(a<b\) are palindromic-prefix lengths, then \(L(j+b-a)\ge L(j)\) for \(1\le j\le a\). Here \(a\) and \(a+p\) can be chosen as large as needed (Step 1), hence \(L(j+p)\ge L(j)\) for **every** \(j\ge1\). The eventual stabilization of Step 3 thus ensures that the global maximum \(M\) is attained in the stable window; in particular the value \(t\) is obtained by the indicated finite scan. Because at least one large prefix is not a palindrome, \(M\ge2\). The unique palindromic-prefix residue has \(L=1\), so it never contributes to \(t\); therefore \(1\le t\le p-1\). For all sufficiently large \(j\), the running maximum equals \(M\) and membership of \(j\) in \(T_w\) is equivalent to \(L(j)=M\). Consequently \(|T_w(N)|=tN/p+O_w(1)\), whereas the single palindromic-prefix residue gives \(P_w(N)=N/p+O_w(1)\). Division yields the claimed ordinary limit \(t\), including the case \(p=2\).

**5. Sharpness for all periods.** Take \(w=(a^rb^s)^\omega\) with \(a\ne b\), \(r,s\ge1\), and \(p=r+s\). The period is primitive since its two cyclic letter changes prevent a smaller period. The positive palindromic-prefix lengths are precisely \(1,\ldots,r\) and \(r+kp\) for integers \(k\ge1\). For every \(n>r\) in the latter residue, \(L(n)=1\). At every other length \(n>r\), \(L(n)=2\): if \(n\pmod p\) lies in \(\{1,\ldots,r-1\}\), split after \(r-(n\pmod p)\) initial \(a\)'s, leaving a palindrome by Step 1; if \(n\pmod p\) is in \(\{r+1,\ldots,p-1\}\), split off its terminal \(b\)-run after the palindromic prefix of length \(r+p\lfloor n/p\rfloor\); and for residue zero split off the final \(b^s\) after a palindromic prefix of length \(n-s\). These cases use exactly two palindromes, and none is a palindrome because of the unique palindromic-prefix residue. Thus \(M=2\) and precisely \(p-1\) stable residues attain it. In fact, for \(N\ge r\),

\[
 P_w(N)=r+\left\lfloor\frac{N-r}{p}\right\rfloor,
 \qquad |T_w(N)|=N-\left\lfloor\frac{N-r}{p}\right\rfloor.
\]

Their quotient tends to \(p-1\), completing the proof.

## Verification

The accompanying `verification.py` computes palindrome intervals by the exact interior recurrence and computes each prefix's minimum palindromic length by the exhaustive recurrence \(L(j)=1+\min_{0\le i<j,\,w[i+1,j]\,\mathrm{palindrome}}L(i)\), with \(L(0)=0\). It checks the specified stabilization threshold and single residue class against 1,030 primitive binary/ternary periodic cases, and checks the two-run family for all splits at periods 2 through 39. `verification_output.txt` records a successful independent execution. These finite checks support the proof but are not a substitute for any of its universal steps. The proof's bound and limit are exact for every permitted \(p\) and every finite alphabet.

## Relationship to prior work

Rukavicka's September 14, 2026 paper established \(|T_w(N)|\ge P_w(N)\) for arbitrary infinite words and its translation lemma. The paper explicitly did not assert an ordinary limit in general, and its example \((ab)^\omega\) yields only the sharp universal lower endpoint. Fischler's 2005 preprint (subsequently 2006 journal article), Lemma 5.6, already establishes precisely one large palindromic-prefix residue for every periodic word with infinitely many palindromic prefixes. These statements are used and credited. The contribution here is the explicit **uniform quadratic cutoff** for the *minimum factorization-length profile*, its **finite determination of the exact ordinary ratio**, and the **sharp full-period upper envelope**. Bucci and Richomme concern *greedy* palindromic length, which is not the minimization used here; Rukavicka's 2020 work concerns lower bounds involving long repeated palindrome blocks and does not give this finite cutoff. No general novelty claim follows solely from unsuccessful indexed searches.

## Limitations

The conclusion is restricted to purely periodic words with infinitely many palindromic prefixes, not arbitrary periodic words lacking that property or aperiodic words. The cutoff is sufficient and is not claimed to be optimal for all periods or all input words. The theorem determines the eventual count \(t\) for a given period by finite computation; it does not classify which intermediate values of \(t\) occur for each \(p\). Only self-review has been performed; publication-priority and independent mathematical validation remain open.

## References

1. Josef Rukavicka, *A lower bound on the density of prefixes with maximal palindromic length*, arXiv:2609.15146v1 (first public September 14, 2026), especially Lemma 6.1, Proposition 6.2, Remark 6.3 and Example 6.4. https://arxiv.org/abs/2609.15146
2. Stéphane Fischler, *Palindromic Prefixes and Episturmian Words*, arXiv:math/0501420v3 (2005), especially Lemma 5.6; J. Combin. Theory Ser. A 113 (2006), 1281–1304. https://arxiv.org/html/math/0501420v3
3. M. Bucci and G. Richomme, *Greedy palindromic lengths*, arXiv:1606.05660, International Journal of Foundations of Computer Science 29 (2018), 331–356. https://arxiv.org/abs/1606.05660
4. Josef Rukavicka, *Palindromic Length of Words with Many Periodic Palindromes*, arXiv:2005.01371 (2020). https://arxiv.org/abs/2005.01371
