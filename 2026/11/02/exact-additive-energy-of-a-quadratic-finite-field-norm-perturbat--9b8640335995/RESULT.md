# Exact additive energy of a quadratic finite-field norm-perturbation value set

## Finding
For every odd prime power \(q\), let \(K=\mathbb F_{q^2}\) and \(k=\mathbb F_q\). Consider the map \(F:K\to K\) given by \(F(x)=x^{q+1}+x\), and its image \(V=F(K)\). Its **additive energy** is
\[
E(V)=\#\{(v_1,v_2,v_3,v_4)\in V^4:v_1+v_2=v_3+v_4\}.
\]
Let \(\chi:k\to\{-1,0,1\}\) be the quadratic character, with \(\chi(0)=0\). Then
\[
\boxed{E(V)=\frac{q^2(q+1)^4+q(q-1)\big((q+1)^2+2q(1+\chi(-1))\big)}{16}.}
\]
The formula distinguishes \(q\equiv1\pmod4\) from \(q\equiv3\pmod4\). It also follows from an exact Fourier spectrum of the image-set indicator.

## Assumptions and scope
The result holds for all odd prime powers, including nonprime fields. Addition is the additive-group operation on \(K\). The energy counts ordered quadruples. No assertion is made in even characteristic.

## Proof
Choose a nonsquare \(d\in k^\times\), and an element \(\omega\in K\) satisfying \(\omega^2=d\). Write \(x=a+b\omega\), with \(a,b\in k\). The field norm is \(N_{K/k}(x)=a^2-db^2\), so
\[
F(a+b\omega)=(a^2+a-db^2)+b\omega.
\]
Consequently, identifying \(K\cong k^2\),
\[
V=\{(u,b):u+db^2+\tfrac14\text{ is a square in }k\},
\]
where zero is included among squares, and \(|V|=q(q+1)/2\). With \(\delta_0(z)=1\) for \(z=0\) and zero otherwise, its indicator is
\[
1_V(u,b)=\tfrac12[1+\chi(u+db^2+\tfrac14)+\delta_0(u+db^2+\tfrac14)].
\]
Fix a nontrivial additive character \(\psi:k\to\mathbb C^\times\) and define the unnormalized Fourier transform
\[
\widehat{1_V}(\xi,\eta)=\sum_{u,b\in k}1_V(u,b)\psi(\xi u+\eta b).
\]
For \(\xi=\eta=0\), it equals \(|V|\); for \(\xi=0\), \(\eta\ne0\), it vanishes by summing first in \(u\). For \(\xi\ne0\), put \(G(\xi)=\sum_{z\in k}\chi(z)\psi(\xi z)\). Translating \(u\) shows that
\[
\widehat{1_V}(\xi,\eta)=\tfrac12\psi(-\xi/4)[1+G(\xi)]\sum_{b\in k}\psi(-\xi db^2+\eta b).
\]
The final quadratic Gauss sum has squared modulus \(q\), because \(\xi d\ne0\). Also \(G(\xi)=\chi(\xi)G(1)\), \(|G(1)|^2=q\), and \(G(1)^2=\chi(-1)q\). Hence
\[
|\widehat{1_V}(\xi,\eta)|^2=\tfrac q4|1+\chi(\xi)G(1)|^2
\quad(\xi\ne0).
\]
In particular, for \(q\equiv3\pmod4\) each nonzero-first-coordinate Fourier magnitude squared equals \(q(q+1)/4\); for \(q\equiv1\pmod4\) its two values are \(q(q+1\pm2\sqrt q)/4\), each attained at exactly \(q(q-1)/2\) frequencies. These statements concern complex absolute values, and \(\sqrt q\) denotes the positive real square root.

The Fourier fourth-moment identity for the additive group \(k^2\) gives
\[
E(V)=q^{-2}\sum_{\xi,\eta\in k}|\widehat{1_V}(\xi,\eta)|^4.
\]
Averaging over the two equally common values of \(\chi(\xi)\) yields
\[
\tfrac12\bigl(|1+G(1)|^4+|1-G(1)|^4\bigr)=(q+1)^2+2q(1+\chi(-1)).
\]
Substituting \(|V|=q(q+1)/2\), and summing the \(q(q-1)\) nonzero-first-coordinate frequencies, yields exactly the boxed formula.

## Verification
Run `python verify_energy.py` with Python 3 and no external dependencies. It independently enumerates the image, its ordered additive pairs, and the resulting fourth-order energy for nine fields, including \(\mathbb F_9\) and \(\mathbb F_{25}\). The command returned `VERIFY_OK fields= 9 total_image_points= 919 total_energy= 24033255`. Finite enumeration checks examples only; the universal assertion rests on the Fourier proof above.

## Relationship to prior work
Kelley and Owen (2015, arXiv:1510.01758) establish bounds on the number of roots of finite-field trinomials. The polynomial fibers of \(x^{q+1}+x\) also belong to the setting of Bluher's 2004 work and to the more general root-solving criteria of Kim, Choe, and Mesnager (2019, arXiv:1912.12648). These studies concern root multiplicities and roots, rather than the additive energy of the entire image, which requires fourth-order additive correlations. Gao and Wang (2014, arXiv:1407.5884) study value-set sizes of random finite-field polynomials, a different invariant. The formula here should not be construed as a new global root count.

## Limitations
Only odd-characteristic finite fields and the specific norm-perturbation polynomial are covered. The proof does not give corresponding higher additive moments or classify all additive representations individually. The 2004 Bluher source could not be inspected in full, and implicit or unlocated published coverage of the additive-energy identity remains a literature risk. Independent external mathematical review has not occurred.

## References
- Z. Kelley and S. W. Owen, *Estimating the Number Of Roots of Trinomials over Finite Fields*, arXiv:1510.01758, first posted 2015-10-06.
- A. W. Bluher, *On \(x^{q+1}+ax+b\)*, Finite Fields and Their Applications 10 (2004), 285–305, doi:10.1016/j.ffa.2003.08.004.
- K. H. Kim, J. Choe and S. Mesnager, *Solving \(X^{q+1}+X+a=0\) over Finite Fields*, arXiv:1912.12648 (2019).
- Z. Gao and Q. Wang, *A probabilistic approach to value sets of polynomials over finite fields*, arXiv:1407.5884 (2014).
