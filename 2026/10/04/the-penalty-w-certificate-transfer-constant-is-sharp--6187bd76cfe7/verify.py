from fractions import Fraction as F

def check(rho, iota, trho):
    assert rho > 0 and iota > 0 and trho > rho
    nu = rho / 2
    base_residual = (rho * iota / 2) / iota
    base_feas_rhs = 2 * iota * nu / rho
    transferred_residual = ((trho - rho / 2) * iota) / iota
    transferred_feas_lb = trho / 2
    proposition = nu + (2 * nu / rho) * (trho - rho)
    assert base_residual == nu
    assert base_feas_rhs == iota
    assert transferred_residual == trho - rho / 2
    assert transferred_residual > transferred_feas_lb
    assert proposition == transferred_residual

for vals in [
    (F(2), F(3), F(5)),
    (F(7,3), F(11,5), F(13,3)),
    (F(5,2), F(1,7), F(9,2)),
]:
    check(*vals)
print("VERIFY_OK")
