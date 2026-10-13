import math

rows = [
    {"name":"dataset1","n":33,"Q":549.37,"AIC_print":537.65,"BIC_print":528.92,"AICc_print":537.80},
    {"name":"dataset2","n":60,"Q":410.34,"AIC_print":411.28,"BIC_print":399.20,"AICc_print":410.33},
]

def criteria(Q,n,p):
    aic=Q+2*p
    bic=Q+p*math.log(n)
    aicc=aic+2*p*(p+1)/(n-p-1)
    return aic,bic,aicc

for r in rows:
    for p in (2,3):
        aic,bic,aicc=criteria(r["Q"],r["n"],p)
        assert abs(aic-r["AIC_print"])>1e-6
        assert abs(bic-r["BIC_print"])>1e-6

# Minimal sign checks for positive-dimensional models.
assert rows[0]["AIC_print"] < rows[0]["Q"]
assert rows[0]["BIC_print"] < rows[0]["Q"]
assert rows[1]["BIC_print"] < rows[1]["Q"]
assert abs((rows[1]["AIC_print"]-rows[1]["Q"])/2 - 0.47) < 1e-12

a1,b1,c1=criteria(549.37,33,3)
a2,b2,c2=criteria(410.34,60,3)
assert abs(a1-555.37)<1e-12
assert abs(b1-559.8595226843994)<1e-12
assert abs(c1-556.1975862068965)<1e-12
assert abs(a2-416.34)<1e-12
assert abs(b2-422.6230336866663)<1e-12
assert abs(c2-416.7685714285714)<1e-12

print("VERIFY_OK")
print("dataset1_p3",format(a1,".12f"),format(b1,".12f"),format(c1,".12f"))
print("dataset2_p3",format(a2,".12f"),format(b2,".12f"),format(c2,".12f"))
print("dataset2_implied_AIC_parameter_count",format((411.28-410.34)/2,".12f"))
